<?php
/**
 * Основные параметры WordPress.
 *
 * Скрипт для создания wp-config.php использует этот файл в процессе
 * установки. Необязательно использовать веб-интерфейс, можно
 * скопировать файл в "wp-config.php" и заполнить значения вручную.
 *
 * Этот файл содержит следующие параметры:
 *
 * * Настройки MySQL
 * * Секретные ключи
 * * Префикс таблиц базы данных
 * * ABSPATH
 *
 * @link https://codex.wordpress.org/Editing_wp-config.php
 *
 * @package WordPress
 */

// ** Параметры MySQL: Эту информацию можно получить у вашего хостинг-провайдера ** //
/** Имя базы данных для WordPress */
define('DB_NAME', 'u1170115_default');

/** Имя пользователя MySQL */
define('DB_USER', 'u1170115_default');

/** Пароль к базе данных MySQL */
define('DB_PASSWORD', 'S30P!Ldc');

/** Имя сервера MySQL */
define( 'DB_HOST', '127.0.0.1' );

/** Кодировка базы данных для создания таблиц. */
define( 'DB_CHARSET', 'utf8mb4' );

/** Схема сопоставления. Не меняйте, если не уверены. */
define( 'DB_COLLATE', '' );

/**#@+
 * Уникальные ключи и соли для аутентификации.
 *
 * Смените значение каждой константы на уникальную фразу.
 * Можно сгенерировать их с помощью {@link https://api.wordpress.org/secret-key/1.1/salt/ сервиса ключей на WordPress.org}
 * Можно изменить их, чтобы сделать существующие файлы cookies недействительными. Пользователям потребуется авторизоваться снова.
 *
 * @since 2.6.0
 */
define( 'AUTH_KEY',         ')D$JRD9)<SgG36lIYz%$Dm&DSqN@IZ5{5-bo{&<oYJ=Jm!.Rikyvl=u[/%>PBY}(' );
define( 'SECURE_AUTH_KEY',  'Jq29~`_>Bkl-A9IQgF]Bl/,KVU[t0Y#e*yB8e>/}SlDb3z{KNBlJzja|d(/-qIe_' );
define( 'LOGGED_IN_KEY',    'MSh^hXcz%.xv{&SM,J[.)ND#l@GjVaXg8@6n<Vh;|l!PIf:lIa4F/KX,f[YF4= F' );
define( 'NONCE_KEY',        'mC4}l}(mGNg/.r.&2+MI^T5x*u!:r,_>3jR-@^K)b!Y/XtSc@:*kGk`N[Uo|}Tx_' );
define( 'AUTH_SALT',        'S#+BB<Ym;>4IuQ4*<D%wLmWb?iJh$ms &adARD3x&l]92~5xk34^drIr:CQ<:-5q' );
define( 'SECURE_AUTH_SALT', 'xs&7bs$.[u%Aktw=?WR4oL]P~w{*VvryN$@9$nT%.%[Gs93F@%N }$4245+HZ@e+' );
define( 'LOGGED_IN_SALT',   '<D:fjp64{@$H)56Wt7S27Q`*<DwF9w]`tS+eLdDj^zSNs:jdigMQFd2^9fe=|Ae8' );
define( 'NONCE_SALT',       'Yupp0X&h^S!&LG~PBEaJ0CS|#:K=;AC$q,lC%&`q=!Onikm{94nRA<+JlavB_bSx' );

/**#@-*/

/**
 * Префикс таблиц в базе данных WordPress.
 *
 * Можно установить несколько сайтов в одну базу данных, если использовать
 * разные префиксы. Пожалуйста, указывайте только цифры, буквы и знак подчеркивания.
 */
$table_prefix = 'wp_';

/**
 * Для разработчиков: Режим отладки WordPress.
 *
 * Измените это значение на true, чтобы включить отображение уведомлений при разработке.
 * Разработчикам плагинов и тем настоятельно рекомендуется использовать WP_DEBUG
 * в своём рабочем окружении.
 *
 * Информацию о других отладочных константах можно найти в Кодексе.
 *
 * @link https://codex.wordpress.org/Debugging_in_WordPress
 */
define( 'WP_DEBUG', false );

/* Это всё, дальше не редактируем. Успехов! */

/** Абсолютный путь к директории WordPress. */
if ( ! defined( 'ABSPATH' ) ) {
	define( 'ABSPATH', dirname( __FILE__ ) . '/' );
}

/** Инициализирует переменные WordPress и подключает файлы. */
require_once( ABSPATH . 'wp-settings.php' );
