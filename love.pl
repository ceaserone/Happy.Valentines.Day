sub love {
    my ($a, $b, $depth) = @_;
    return "Love persists beyond limits.\n" if $depth > 10; # our love is infinite babes

    print "$a supports $b ❤️\n";
    print "$b supports $a ❤️\n";

    love($a, $b, $depth + 1);  # Love grows with time (sometimes ez sometimes hard)
}

love("You", "Me", 0);
