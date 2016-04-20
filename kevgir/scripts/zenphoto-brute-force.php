<?php
    function pbkdf2($p, $s, $c = 1000, $kl = 32, $a = 'sha256') {
        $hl = strlen(hash($a, null, true)); # Hash length
        $kb = ceil($kl / $hl); # Key blocks to compute
        $dk = ''; # Derived key
        # Create key
        for ($block = 1; $block <= $kb; $block++) {
            # Initial hash for this block
            $ib = $b = hash_hmac($a, $s . pack('N', $block), $p, true);
            # Perform block iterations
            for ($i = 1; $i < $c; $i++)
            # XOR each iterate
            $ib ^= ($b = hash_hmac($a, $b, $p, true));
            $dk .= $ib; # Append iterated block
        }
        # Return derived key of correct length
        return substr($dk, 0, $kl);
    }

    $hash_ref = "nT/y9QPmdknO/pu7QI4kNZK3yVk3h/Lan5M6mWLTE4I=";
    $user = "travis";
    $salt = "0@n6AraXM~L8pQ/&eOY=cHGw52l(q!";
    $min_pass_len = 6;
    $wl = "rockyou.txt";

    $fp = fopen($wl, "r");
    if ($fp) {
        while (($line = fgets($fp)) !== false) {
            $pass = trim($line);
            if ( strlen($pass) >= $min_pass_len ){
                $hash = str_replace('+', '-', base64_encode(pbkdf2($pass, $user . $salt)));
                if ( strcmp($hash, $hash_ref) == 0 ) {
                    echo "Found: " . $pass;
                    exit(0);
                } else {
                    echo "Trying with: " . $hash . "\r";
                }
            }
        }
        fclose($fp);
    }
?>
