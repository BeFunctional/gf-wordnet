{
  description = "Grammatical Framework's Wordnet library";

  inputs.flake-utils.url = "github:numtide/flake-utils";
  
  inputs.gf-core.url ="github:BeFunctional/gf-core?ref=tp_nix_flake";
  inputs.gf-rgl.url = "github:BeFunctional/gf-rgl?ref=tp_flake";

  outputs = { self, nixpkgs, flake-utils, gf-core, gf-rgl }: 
    flake-utils.lib.eachDefaultSystem (system:
      let
        pkgs = nixpkgs.legacyPackages.${system};
      in
      {
        defaultPackage = pkgs.stdenv.mkDerivation {
          name = "gf-wordnet";
          src = ./.;
          GF_LIB_PATH = gf-rgl.defaultPackage.${system};
          buildInputs = [gf-core.packages.${system}.gf];

          buildPhase = ''
            mkdir -p build
            find . -name 'WordNet*.gf' -print0 | xargs -0 -n 1 -P 16 gf --output-dir=build
          '';
          installPhase = ''
            mkdir -p $out
            cp -r build $out/
          '';
        };
      }
    );
}