
let
  pkgs = import <nixpkgs> {};
  dev_config = import ./.idx/dev.nix { inherit pkgs; };
in
pkgs.mkShell {
  buildInputs = dev_config.packages;
}
