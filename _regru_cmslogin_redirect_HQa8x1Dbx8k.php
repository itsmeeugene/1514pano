<?php setrawcookie( "wordpress_test_cookie", "WP+Cookie+check" ); ?>
    <html>
    <script>
      function formSubmit() {
        var loginForm = document.getElementById("loginform");
        loginForm.submit();
      }
    </script>
    <body onload="formSubmit()">
      <form name="loginform" id="loginform" action="/wp-login.php" method="post">
        <input type="hidden" name="log" value="<?php print $_POST["login"]; ?>">
        <input type="hidden" name="pwd" value="<?php print $_POST["pass"]; ?>">
        <input type="hidden" name="redirect_to" value="<?php if ( $_POST["divi"] ) { print "/?et_fb=1&PageSpeed=off"; } else { print "/wp-admin/"; }; ?>">
        <input type="hidden" name="testcookie" value="0">
        <input type="submit" name="wp-submit" value="Redirecting to WordPress Site ...">
      </form>    
    </body>