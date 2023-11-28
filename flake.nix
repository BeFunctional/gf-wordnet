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

            find . -name 'WordNet*.gf' -exec gf {} \;
          '';
          installPhase = ''
            mkdir -p $out
            cp -r *.gf $out
            cp -r *.gfo $out
          '';
        };
      }
    );
}