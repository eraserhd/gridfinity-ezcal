{
  description = "TODO: fill me in";
  inputs = {
    nixpkgs.url = "github:NixOS/nixpkgs/nixos-unstable";
    flake-utils.url = "github:numtide/flake-utils";
    poetry2nix.url = "github:nix-community/poetry2nix";
  };
  outputs = { self, nixpkgs, poetry2nix, flake-utils }:
    (flake-utils.lib.eachDefaultSystem (system:
      let
        pkgs = nixpkgs.legacyPackages.${system};
        p2n = poetry2nix.lib.mkPoetry2Nix { inherit pkgs; };
        pythonEnv = p2n.mkPoetryEnv {
          projectDir = ./.;
          overrides = p2n.overrides.withDefaults (final: prev: {
            ocpsvg = prev.ocpsvg.overridePythonAttrs (old: {
              nativeBuildInputs = (old.nativeBuildInputs or []) ++ [final.setuptools];
            });
            svgpathtools = prev.svgpathtools.overridePythonAttrs (old: {
              nativeBuildInputs = (old.nativeBuildInputs or []) ++ [final.setuptools];
            });
            trianglesolver = prev.trianglesolver.overridePythonAttrs (old: {
              nativeBuildInputs = (old.nativeBuildInputs or []) ++ [final.setuptools];
            });
          });
        };
      in {
        devShells.default = pkgs.mkShell {
          nativeBuildInputs = [
            pythonEnv
            pkgs.poetry
            pkgs.python3
            pkgs.python3Packages.ipython
          ];
        };
    }));
}
