{
  description = "TODO: fill me in";
  inputs = {
    flake-utils.url = "github:numtide/flake-utils";
  };
  outputs = { self, nixpkgs, flake-utils }:
    (flake-utils.lib.eachDefaultSystem (system:
      let
        pkgs = nixpkgs.legacyPackages.${system};
        gridfinity-ezcal = pkgs.callPackage ./derivation.nix {};
      in {
        packages = {
          default = gridfinity-ezcal;
          inherit gridfinity-ezcal;
        };
        checks = {
          test = pkgs.runCommandNoCC "gridfinity-ezcal-test" {} ''
            mkdir -p $out
            : ${gridfinity-ezcal}
          '';
        };
    })) // {
      overlays.default = final: prev: {
        gridfinity-ezcal = prev.callPackage ./derivation.nix {};
      };
    };
}
