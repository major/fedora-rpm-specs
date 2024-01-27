#
# Fedora spec file for php-symfony
#
# Copyright (c) 2013-2019 Shawn Iwinski <shawn.iwinski@gmail.com>
#                         Remi Collet <remi@fedoraproject.org>
#
# License: MIT
# http://opensource.org/licenses/MIT
#
# Please preserve changelog entries
#

%global github_owner     symfony
%global github_name      symfony
%global github_version   2.8.52
%global github_commit    88f3ef62d6ab870128352c8686c7889562698faf
%global github_short     %(c=%{github_commit}; echo ${c:0:7})

%global composer_vendor  symfony
%global composer_project symfony

# "php": ">=5.3.9"
# to avoid symfony-polyfill
%global php_min_ver 7.0
# "doctrine/annotations": "~1.0"
#     src/Symfony/Bundle/FrameworkBundle/composer.json
#     src/Symfony/Component/PropertyInfo/composer.json
#     src/Symfony/Component/Routing/composer.json
#     src/Symfony/Component/Serializer/composer.json
#     src/Symfony/Component/Validator/composer.json
%global doctrine_annotations_min_ver 1.0
%global doctrine_annotations_max_ver 2.0
# "doctrine/cache": "~1.0"
#     src/Symfony/Bundle/FrameworkBundle/composer.json
#     src/Symfony/Component/Serializer/composer.json
#     src/Symfony/Component/Validator/composer.json
%global doctrine_cache_min_ver 1.0
%global doctrine_cache_max_ver 2.0
# "doctrine/common": "~2.4"
%global doctrine_common_min_ver 2.4
%global doctrine_common_max_ver 3.0
# "doctrine/data-fixtures": "1.0.*"
# ignore max version
%global doctrine_datafixtures_min_ver 1.0.0
%global doctrine_datafixtures_max_ver 2
# "doctrine/dbal": "~2.4"
#     NOTE: Min version not 2.4 because autoloader required
%global doctrine_dbal_min_ver 2.5.4
%global doctrine_dbal_max_ver 3.0
# "doctrine/doctrine-bundle": "~1.2"
%global doctrine_bundle_min_ver 1.2
%global doctrine_bundle_max_ver 2.0
# "doctrine/orm": "~2.4,>=2.4.5"
%global doctrine_orm_min_ver 2.4.5
%global doctrine_orm_max_ver 3.0
# "egulias/email-validator": "~1.2,>=1.2.1"
%global email_validator_min_ver 1.2.1
%global email_validator_max_ver 2.0
# "monolog/monolog": "~1.11"
#     NOTE: Min version not 1.11 because autoloader required
%global monolog_min_ver 1.15.0
%global monolog_max_ver 2.0
# "ocramius/proxy-manager": "~0.4|~1.0|~2.0"
%global proxy_manager_min_ver 1.0
%global proxy_manager_max_ver 3.0
# "phpdocumentor/reflection": "^1.0.7"
%global phpdocumentor_reflection_min_ver 1.0.7
%global phpdocumentor_reflection_max_ver 2.0
# "psr/log": "~1.0"
#     NOTE: Min version not 1.0 because autoloader required
%global psr_log_min_ver 1.0.1
%global psr_log_max_ver 2.0
# "swiftmailer/swiftmailer": ">=4.2.0,<6.0-dev"
#     src/Symfony/Bridge/Swiftmailer/composer.json
#     NOTE: Min version not 4.2.0 because autoloader required
%global swiftmailer_min_ver 5.4.1
%global swiftmailer_max_ver 6.0
# "symfony/polyfill-php54": "~1.0"
# "symfony/polyfill-php55": "~1.0"
# "symfony/polyfill-php56": "~1.8"
# "symfony/polyfill-php70": "~1.0"
# "symfony/polyfill-util": "~1.0"
%global symfony_polyfill_min_ver 1.8
%global symfony_polyfill_max_ver 2.0
# "symfony/security-acl": "~2.7|~3.0.0"
%global symfony_security_acl_min_ver 2.7
%global symfony_security_acl_max_ver 4
# "twig/twig": "~1.34|~2.4"
%global twig_min_ver 1.34
%global twig_max_ver 3.0

# Build using "--with tests" to enable tests
%global with_tests   0%{?_with_tests:1}

%if 0%{?fedora} >= 27 || 0%{?rhel} >= 8
%global with_range_dependencies 1
%else
%global with_range_dependencies 0
%endif

%{!?phpdir:  %global phpdir  %{_datadir}/php}

%global symfony_dir  %{phpdir}/Symfony
%global pear_channel pear.symfony.com

Name:          php-%{composer_project}
Version:       %{github_version}
Release:       13%{?dist}
Summary:       PHP framework for web projects

License:       MIT
URL:           https://symfony.com
Source0:       https://github.com/%{github_owner}/%{github_name}/archive/%{github_commit}/%{name}-%{github_version}-%{github_short}.tar.gz

BuildArch:     noarch
## composer.json
# Force version to 4.8 for autoloader
BuildRequires: php-composer(phpunit/phpunit)          >= 4.8
BuildRequires: php(language)                          >= %{php_min_ver}
%if %{with_range_dependencies}
BuildRequires: (php-composer(doctrine/annotations) >= %{doctrine_annotations_min_ver} with php-composer(doctrine/annotations) < %{doctrine_annotations_max_ver})
BuildRequires: (php-composer(doctrine/cache) >= %{doctrine_cache_min_ver} with php-composer(doctrine/cache) < %{doctrine_cache_max_ver})
BuildRequires: (php-composer(doctrine/common) >= %{doctrine_common_min_ver} with php-composer(doctrine/common) < %{doctrine_common_max_ver})
BuildRequires: (php-composer(doctrine/data-fixtures) >= %{doctrine_datafixtures_min_ver} with php-composer(doctrine/data-fixtures) < %{doctrine_datafixtures_max_ver})
BuildRequires: (php-composer(doctrine/dbal) >= %{doctrine_dbal_min_ver} with php-composer(doctrine/dbal) < %{doctrine_dbal_max_ver})
BuildRequires: (php-composer(doctrine/doctrine-bundle) >= %{doctrine_bundle_min_ver} with php-composer(doctrine/doctrine-bundle) < %{doctrine_bundle_max_ver})
BuildRequires: (php-composer(doctrine/orm) >= %{doctrine_orm_min_ver} with php-composer(doctrine/orm) < %{doctrine_orm_max_ver})
BuildRequires: (php-composer(egulias/email-validator) >= %{email_validator_min_ver} with php-composer(egulias/email-validator) < %{email_validator_max_ver})
BuildRequires: (php-composer(monolog/monolog) >= %{monolog_min_ver} with php-composer(monolog/monolog) < %{monolog_max_ver})
BuildRequires: (php-composer(ocramius/proxy-manager) >= %{proxy_manager_min_ver} with php-composer(ocramius/proxy-manager) < %{proxy_manager_max_ver})
BuildRequires: (php-composer(phpdocumentor/reflection) >= %{phpdocumentor_reflection_min_ver} with php-composer(phpdocumentor/reflection) < %{phpdocumentor_reflection_max_ver})
BuildRequires: (php-composer(psr/log) >= %{psr_log_min_ver} with php-composer(psr/log) < %{psr_log_max_ver})
BuildRequires: (php-composer(swiftmailer/swiftmailer) >= %{swiftmailer_min_ver} with php-composer(swiftmailer/swiftmailer) < %{swiftmailer_max_ver})
BuildRequires: (php-composer(symfony/polyfill-util) >= %{symfony_polyfill_min_ver} with php-composer(symfony/polyfill-util) < %{symfony_polyfill_max_ver})
BuildRequires: (php-composer(symfony/security-acl) >= %{symfony_security_acl_min_ver} with php-composer(symfony/security-acl) < %{symfony_security_acl_max_ver})
BuildRequires: (php-composer(twig/twig) >= %{twig_min_ver} with php-composer(twig/twig) < %{twig_max_ver})
%else
BuildRequires: php-composer(doctrine/annotations)     <  %{doctrine_annotations_max_ver}
BuildRequires: php-composer(doctrine/annotations)     >= %{doctrine_annotations_min_ver}
BuildRequires: php-composer(doctrine/cache)           <  %{doctrine_cache_max_ver}
BuildRequires: php-composer(doctrine/cache)           >= %{doctrine_cache_min_ver}
BuildRequires: php-composer(doctrine/common)          <  %{doctrine_common_max_ver}
BuildRequires: php-composer(doctrine/common)          >= %{doctrine_common_min_ver}
BuildRequires: php-composer(doctrine/data-fixtures)   <  %{doctrine_datafixtures_max_ver}
BuildRequires: php-composer(doctrine/data-fixtures)   >= %{doctrine_datafixtures_min_ver}
BuildRequires: php-composer(doctrine/dbal)            <  %{doctrine_dbal_max_ver}
BuildRequires: php-composer(doctrine/dbal)            >= %{doctrine_dbal_min_ver}
BuildRequires: php-composer(doctrine/doctrine-bundle) <  %{doctrine_bundle_max_ver}
BuildRequires: php-composer(doctrine/doctrine-bundle) >= %{doctrine_bundle_min_ver}
BuildRequires: php-composer(doctrine/orm)             <  %{doctrine_orm_max_ver}
BuildRequires: php-composer(doctrine/orm)             >= %{doctrine_orm_min_ver}
BuildRequires: php-composer(egulias/email-validator)  <  %{email_validator_max_ver}
BuildRequires: php-composer(egulias/email-validator)  >= %{email_validator_min_ver}
BuildRequires: php-composer(monolog/monolog)          <  %{monolog_max_ver}
BuildRequires: php-composer(monolog/monolog)          >= %{monolog_min_ver}
BuildRequires: php-composer(ocramius/proxy-manager)   <  %{proxy_manager_max_ver}
BuildRequires: php-composer(ocramius/proxy-manager)   >= %{proxy_manager_min_ver}
BuildRequires: php-composer(phpdocumentor/reflection) <  %{phpdocumentor_reflection_max_ver}
BuildRequires: php-composer(phpdocumentor/reflection) >= %{phpdocumentor_reflection_min_ver}
BuildRequires: php-composer(psr/log)                  <  %{psr_log_max_ver}
BuildRequires: php-composer(psr/log)                  >= %{psr_log_min_ver}
BuildRequires: php-composer(swiftmailer/swiftmailer)  <  %{swiftmailer_max_ver}
BuildRequires: php-composer(swiftmailer/swiftmailer)  >= %{swiftmailer_min_ver}
BuildRequires: php-composer(symfony/polyfill-util)    <  %{symfony_polyfill_max_ver}
BuildRequires: php-composer(symfony/polyfill-util)    >= %{symfony_polyfill_min_ver}
BuildRequires: php-composer(symfony/security-acl)     <  %{symfony_security_acl_max_ver}
BuildRequires: php-composer(symfony/security-acl)     >= %{symfony_security_acl_min_ver}
### See twig-bridge
%if 0%{?fedora} < 25 && 0%{?rhel} < 8
BuildRequires: php-composer(twig/twig)                <  2
%else
BuildRequires: php-composer(twig/twig)                <  %{twig_max_ver}
%endif
BuildRequires: php-composer(twig/twig)                >= %{twig_min_ver}
%endif
## phpcompatinfo (computed from version 2.8.6)
BuildRequires: php-ctype
BuildRequires: php-curl
BuildRequires: php-date
BuildRequires: php-dom
BuildRequires: php-fileinfo
BuildRequires: php-filter
BuildRequires: php-gd
BuildRequires: php-hash
BuildRequires: php-iconv
BuildRequires: php-intl
BuildRequires: php-json
BuildRequires: php-ldap
BuildRequires: php-libxml
BuildRequires: php-mbstring
BuildRequires: php-pcntl
BuildRequires: php-pcre
BuildRequires: php-pdo
BuildRequires: php-posix
BuildRequires: php-readline
BuildRequires: php-reflection
BuildRequires: php-session
BuildRequires: php-simplexml
BuildRequires: php-sockets
BuildRequires: php-spl
BuildRequires: php-sqlite3
BuildRequires: php-tokenizer
BuildRequires: php-xml

# Bridges
Requires:      php-composer(%{composer_vendor}/doctrine-bridge)      = %{version}
Requires:      php-composer(%{composer_vendor}/monolog-bridge)       = %{version}
%if 0%{?fedora} >= 26 || 0%{?rhel} >= 8
# this requires ZF and thus PHP 7
Requires:      php-composer(%{composer_vendor}/proxy-manager-bridge) = %{version}
%endif
Requires:      php-composer(%{composer_vendor}/swiftmailer-bridge)   = %{version}
Requires:      php-composer(%{composer_vendor}/twig-bridge)          = %{version}
# Bundles
Requires:      php-composer(%{composer_vendor}/debug-bundle)         = %{version}
Requires:      php-composer(%{composer_vendor}/framework-bundle)     = %{version}
Requires:      php-composer(%{composer_vendor}/security-bundle)      = %{version}
Requires:      php-composer(%{composer_vendor}/twig-bundle)          = %{version}
Requires:      php-composer(%{composer_vendor}/web-profiler-bundle)  = %{version}
# Components
Requires:      php-composer(%{composer_vendor}/asset)                = %{version}
Requires:      php-composer(%{composer_vendor}/browser-kit)          = %{version}
Requires:      php-composer(%{composer_vendor}/class-loader)         = %{version}
Requires:      php-composer(%{composer_vendor}/config)               = %{version}
Requires:      php-composer(%{composer_vendor}/console)              = %{version}
Requires:      php-composer(%{composer_vendor}/css-selector)         = %{version}
Requires:      php-composer(%{composer_vendor}/debug)                = %{version}
Requires:      php-composer(%{composer_vendor}/dependency-injection) = %{version}
Requires:      php-composer(%{composer_vendor}/dom-crawler)          = %{version}
Requires:      php-composer(%{composer_vendor}/event-dispatcher)     = %{version}
Requires:      php-composer(%{composer_vendor}/expression-language)  = %{version}
Requires:      php-composer(%{composer_vendor}/filesystem)           = %{version}
Requires:      php-composer(%{composer_vendor}/finder)               = %{version}
Requires:      php-composer(%{composer_vendor}/form)                 = %{version}
Requires:      php-composer(%{composer_vendor}/http-foundation)      = %{version}
Requires:      php-composer(%{composer_vendor}/http-kernel)          = %{version}
Requires:      php-composer(%{composer_vendor}/intl)                 = %{version}
Requires:      php-composer(%{composer_vendor}/ldap)                 = %{version}
Requires:      php-composer(%{composer_vendor}/locale)               = %{version}
Requires:      php-composer(%{composer_vendor}/options-resolver)     = %{version}
Requires:      php-composer(%{composer_vendor}/process)              = %{version}
Requires:      php-composer(%{composer_vendor}/property-access)      = %{version}
Requires:      php-composer(%{composer_vendor}/property-info)        = %{version}
Requires:      php-composer(%{composer_vendor}/routing)              = %{version}
Requires:      php-composer(%{composer_vendor}/security)             = %{version}
Requires:      php-composer(%{composer_vendor}/serializer)           = %{version}
Requires:      php-composer(%{composer_vendor}/stopwatch)            = %{version}
Requires:      php-composer(%{composer_vendor}/templating)           = %{version}
Requires:      php-composer(%{composer_vendor}/translation)          = %{version}
Requires:      php-composer(%{composer_vendor}/validator)            = %{version}
Requires:      php-composer(%{composer_vendor}/var-dumper)           = %{version}
Requires:      php-composer(%{composer_vendor}/yaml)                 = %{version}

# Composer
Provides:      php-composer(%{composer_vendor}/%{composer_project})  = %{version}

%description
%{summary}

# ##############################################################################

%package   common

Summary:   Symfony common files

Requires:  php(language)        >= %{php_min_ver}
# Autoloader
Requires:  %{name}-class-loader =  %{version}-%{release}

Obsoletes: php-channel-symfony2

%description common
%{summary}

# ------------------------------------------------------------------------------

%package  doctrine-bridge

Summary:  Symfony Doctrine Bridge

# composer.json
%if %{with_range_dependencies}
Requires: (php-composer(doctrine/common) >= %{doctrine_common_min_ver} with php-composer(doctrine/common) < %{doctrine_common_max_ver})
%else
Requires: php-composer(doctrine/common)                  <  %{doctrine_common_max_ver}
Requires: php-composer(doctrine/common)                  >= %{doctrine_common_min_ver}
%endif
# composer.json: optional
Requires: php-composer(%{composer_vendor}/form)          =  %{version}
Requires: php-composer(%{composer_vendor}/property-info) =  %{version}
Requires: php-composer(%{composer_vendor}/validator)     =  %{version}
%if %{with_range_dependencies}
Requires: (php-composer(doctrine/data-fixtures) >= %{doctrine_datafixtures_min_ver} with php-composer(doctrine/data-fixtures) < %{doctrine_datafixtures_max_ver})
Requires: (php-composer(doctrine/dbal) >= %{doctrine_dbal_min_ver} with php-composer(doctrine/dbal) < %{doctrine_dbal_max_ver})
Requires: (php-composer(doctrine/orm) >= %{doctrine_orm_min_ver} with php-composer(doctrine/orm) < %{doctrine_orm_max_ver})
%else
Requires: php-composer(doctrine/data-fixtures)           <  %{doctrine_datafixtures_max_ver}
Requires: php-composer(doctrine/data-fixtures)           >= %{doctrine_datafixtures_min_ver}
Requires: php-composer(doctrine/dbal)                    <  %{doctrine_dbal_max_ver}
Requires: php-composer(doctrine/dbal)                    >= %{doctrine_dbal_min_ver}
Requires: php-composer(doctrine/orm)                     <  %{doctrine_orm_max_ver}
Requires: php-composer(doctrine/orm)                     >= %{doctrine_orm_min_ver}
%endif
# phpcompatinfo (computed from version 2.8.6)
Requires: php-ctype
Requires: php-date
Requires: php-hash
Requires: php-json
Requires: php-mbstring
Requires: php-pcre
Requires: php-reflection
Requires: php-session
Requires: php-spl

# Composer
Provides: php-composer(%{composer_vendor}/doctrine-bridge) = %{version}
# PEAR
Provides: php-pear(%{pear_channel}/DoctrineBridge) = %{version}
# Rename
Obsoletes: %{name}-doctrinebridge < %{version}
Provides:  %{name}-doctrinebridge = %{version}

%description doctrine-bridge
Provides integration for Doctrine (http://www.doctrine-project.org/) with
various Symfony components.

Configuration reference:
http://symfony.com/doc/2.8/reference/configuration/doctrine.html

# ------------------------------------------------------------------------------

%package  monolog-bridge

Summary:  Symfony Monolog Bridge

# composer.json
%if %{with_range_dependencies}
Requires: (php-composer(monolog/monolog) >= %{monolog_min_ver} with php-composer(monolog/monolog) < %{monolog_max_ver})
%else
Requires: php-composer(monolog/monolog) <  %{monolog_max_ver}
Requires: php-composer(monolog/monolog) >= %{monolog_min_ver}
%endif
# composer.json: optional
Requires: php-composer(%{composer_vendor}/console)          = %{version}
Requires: php-composer(%{composer_vendor}/event-dispatcher) = %{version}
Requires: php-composer(%{composer_vendor}/http-kernel)      = %{version}
# phpcompatinfo (computed from version 2.8.6)
Requires: php-pcre
Requires: php-reflection
Requires: php-date

# Composer
Provides: php-composer(%{composer_vendor}/monolog-bridge) = %{version}
# PEAR
Provides: php-pear(%{pear_channel}/MonologBridge) = %{version}
# Rename
Obsoletes: %{name}-monologbridge < %{version}
Provides:  %{name}-monologbridge = %{version}

%description monolog-bridge
Provides integration for Monolog (https://github.com/Seldaek/monolog) with
various Symfony components.

Configuration reference:
http://symfony.com/doc/2.8/reference/configuration/monolog.html

# ------------------------------------------------------------------------------

%package  phpunit-bridge

Summary:  Symfony PHPUnit Bridge

Requires: %{name}-common = %{version}-%{release}
# phpcompatinfo (computed from version 2.8.6)
Requires: php-date
Requires: php-pcre
Requires: php-posix
Requires: php-reflection

# Composer
Provides: php-composer(%{composer_vendor}/phpunit-bridge) = %{version}

%description phpunit-bridge
Provides utilities for PHPUnit, especially user deprecation notices management.

It comes with the following features:
* disable the garbage collector
* auto-register class_exists to load Doctrine annotations
* print a user deprecation notices summary at the end of the test suite.

Optional:
* php-symfony-debug:
      For tracking deprecated interfaces usages at runtime with DebugClassLoader

# ------------------------------------------------------------------------------

%package  proxy-manager-bridge

Summary:  Symfony ProxyManager Bridge

# composer.json
Requires: php-composer(%{composer_vendor}/dependency-injection) =  %{version}
%if %{with_range_dependencies}
Requires: (php-composer(ocramius/proxy-manager) >= %{proxy_manager_min_ver} with php-composer(ocramius/proxy-manager) < %{proxy_manager_max_ver})
%else
Requires: php-composer(ocramius/proxy-manager)                  <  %{proxy_manager_max_ver}
Requires: php-composer(ocramius/proxy-manager)                  >= %{proxy_manager_min_ver}
%endif
# phpcompatinfo (computed from version 2.8.6)
Requires: php-reflection
Requires: php-spl

# Composer
Provides: php-composer(%{composer_vendor}/proxy-manager-bridge) = %{version}

%description proxy-manager-bridge
Provides integration for ProxyManager [1] with various Symfony components.

[1] http://ocramius.github.io/ProxyManager/

# ------------------------------------------------------------------------------

%package  swiftmailer-bridge

Summary:  Symfony Swiftmailer Bridge

# composer.json
%if %{with_range_dependencies}
Requires: (php-composer(swiftmailer/swiftmailer) >= %{swiftmailer_min_ver} with php-composer(swiftmailer/swiftmailer) < %{swiftmailer_max_ver})
%else
Requires: php-composer(swiftmailer/swiftmailer) <  %{swiftmailer_max_ver}
Requires: php-composer(swiftmailer/swiftmailer) >= %{swiftmailer_min_ver}
%endif
# composer.json: optional
Requires: php-composer(%{composer_vendor}/http-kernel) = %{version}
# phpcompatinfo (computed from version 2.8.6)
# <none>

# Composer
Provides: php-composer(%{composer_vendor}/swiftmailer-bridge) = %{version}
# Rename
Obsoletes: %{name}-swiftmailerbridge < %{version}
Provides:  %{name}-swiftmailerbridge = %{version}

%description swiftmailer-bridge
Provides integration for Swift Mailer (http://swiftmailer.org/) with various
Symfony components.

NOTE: Deprecated since version 2.4, to be removed in 3.0. Use SwiftmailerBundle
instead.

# ------------------------------------------------------------------------------

%package  twig-bridge

Summary:  Symfony Twig Bridge

# composer.json
%if %{with_range_dependencies}
Requires: (php-composer(twig/twig) >= %{twig_min_ver} with php-composer(twig/twig) < %{twig_max_ver})
%else
%if 0%{?fedora} < 25 && 0%{?rhel} < 8
Requires: php-composer(twig/twig)                              <  2
%else
Requires: php-composer(twig/twig)                              <  %{twig_max_ver}
%endif
Requires: php-composer(twig/twig)                              >= %{twig_min_ver}
%endif
# composer.json: optional
Requires: php-composer(%{composer_vendor}/asset)               =  %{version}
Requires: php-composer(%{composer_vendor}/expression-language) =  %{version}
Requires: php-composer(%{composer_vendor}/finder)              =  %{version}
Requires: php-composer(%{composer_vendor}/form)                =  %{version}
Requires: php-composer(%{composer_vendor}/http-kernel)         =  %{version}
Requires: php-composer(%{composer_vendor}/routing)             =  %{version}
Requires: php-composer(%{composer_vendor}/security)            =  %{version}
Requires: php-composer(%{composer_vendor}/stopwatch)           =  %{version}
Requires: php-composer(%{composer_vendor}/templating)          =  %{version}
Requires: php-composer(%{composer_vendor}/translation)         =  %{version}
Requires: php-composer(%{composer_vendor}/var-dumper)          =  %{version}
Requires: php-composer(%{composer_vendor}/yaml)                =  %{version}
# phpcompatinfo (computed from version 2.8.6)
Requires: php-json
Requires: php-pcre
Requires: php-reflection
Requires: php-spl

# Composer
Provides: php-composer(%{composer_vendor}/twig-bridge) = %{version}
# PEAR
Provides: php-pear(%{pear_channel}/TwigBridge) = %{version}
# Rename
Obsoletes: %{name}-twigbridge < %{version}
Provides:  %{name}-twigbridge = %{version}

%description twig-bridge
Provides integration for Twig (http://twig.sensiolabs.org/) with various
Symfony components.

Configuration reference:
http://symfony.com/doc/2.8/reference/configuration/twig.html

# ------------------------------------------------------------------------------

%package  debug-bundle

Summary:  Symfony Debug Bundle

# composer.json
Requires: php-composer(%{composer_vendor}/http-kernel)          = %{version}
Requires: php-composer(%{composer_vendor}/twig-bridge)          = %{version}
Requires: php-composer(%{composer_vendor}/var-dumper)           = %{version}
# composer.json: optional
Requires: php-composer(%{composer_vendor}/config)               = %{version}
Requires: php-composer(%{composer_vendor}/dependency-injection) = %{version}
# phpcompatinfo (computed from version 2.8.6)
# <none>

# Composer
Provides: php-composer(%{composer_vendor}/debug-bundle) = %{version}

%description debug-bundle
%{summary}.

Configuration reference:
http://symfony.com/doc/2.8/reference/configuration/debug.html

# ------------------------------------------------------------------------------

%package  framework-bundle

Summary:  Symfony Framework Bundle

# composer.json
Requires: php-xml
Requires: php-composer(%{composer_vendor}/asset)                =  %{version}
Requires: php-composer(%{composer_vendor}/class-loader)         =  %{version}
Requires: php-composer(%{composer_vendor}/config)               =  %{version}
Requires: php-composer(%{composer_vendor}/dependency-injection) =  %{version}
Requires: php-composer(%{composer_vendor}/event-dispatcher)     =  %{version}
Requires: php-composer(%{composer_vendor}/filesystem)           =  %{version}
Requires: php-composer(%{composer_vendor}/finder)               =  %{version}
Requires: php-composer(%{composer_vendor}/http-foundation)      =  %{version}
Requires: php-composer(%{composer_vendor}/http-kernel)          =  %{version}
Requires: php-composer(%{composer_vendor}/routing)              =  %{version}
Requires: php-composer(%{composer_vendor}/security-core)        =  %{version}
Requires: php-composer(%{composer_vendor}/security-csrf)        =  %{version}
Requires: php-composer(%{composer_vendor}/stopwatch)            =  %{version}
Requires: php-composer(%{composer_vendor}/templating)           =  %{version}
Requires: php-composer(%{composer_vendor}/translation)          =  %{version}
%if %{with_range_dependencies}
Requires: (php-composer(doctrine/annotations) >= %{doctrine_annotations_min_ver} with php-composer(doctrine/annotations) < %{doctrine_annotations_max_ver})
Requires: (php-composer(doctrine/cache) >= %{doctrine_cache_min_ver} with php-composer(doctrine/cache) < %{doctrine_cache_max_ver})
%else
Requires: php-composer(doctrine/annotations)                    <  %{doctrine_annotations_max_ver}
Requires: php-composer(doctrine/annotations)                    >= %{doctrine_annotations_min_ver}
Requires: php-composer(doctrine/cache)                          <  %{doctrine_cache_max_ver}
Requires: php-composer(doctrine/cache)                          >= %{doctrine_cache_min_ver}
%endif
# composer.json: optional
Requires: php-composer(%{composer_vendor}/console)              =  %{version}
Requires: php-composer(%{composer_vendor}/form)                 =  %{version}
Requires: php-composer(%{composer_vendor}/process)              =  %{version}
Requires: php-composer(%{composer_vendor}/property-info)        =  %{version}
Requires: php-composer(%{composer_vendor}/serializer)           =  %{version}
Requires: php-composer(%{composer_vendor}/validator)            =  %{version}
Requires: php-composer(%{composer_vendor}/yaml)                 =  %{version}
# phpcompatinfo (computed from version 2.8.6)
Requires: php-dom
Requires: php-fileinfo
Requires: php-filter
Requires: php-hash
Requires: php-json
Requires: php-mbstring
Requires: php-pcntl
Requires: php-pcre
Requires: php-posix
Requires: php-reflection
Requires: php-spl
Requires: php-tokenizer

# Composer
Provides: php-composer(%{composer_vendor}/framework-bundle) = %{version}
# Rename
Obsoletes: %{name}-frameworkbundle < %{version}
Provides:  %{name}-frameworkbundle = %{version}

%description framework-bundle
The FrameworkBundle contains most of the "base" framework functionality and can
be configured under the framework key in your application configuration. This
includes settings related to sessions, translation, forms, validation, routing
and more.

Configuration reference:
http://symfony.com/doc/2.8/reference/configuration/framework.html

# ------------------------------------------------------------------------------

%package  security-bundle

Summary:  Symfony Security Bundle

# composer.json
Requires: php-composer(%{composer_vendor}/http-kernel) =  %{version}
Requires: php-composer(%{composer_vendor}/security)    =  %{version}
%if %{with_range_dependencies}
Requires: (php-composer(symfony/security-acl) >= %{symfony_security_acl_min_ver} with php-composer(symfony/security-acl) < %{symfony_security_acl_max_ver})
%else
Requires: php-composer(symfony/security-acl)           <  %{symfony_security_acl_max_ver}
Requires: php-composer(symfony/security-acl)           >= %{symfony_security_acl_min_ver}
%endif
# phpcompatinfo (computed from version 2.8.6)
Requires: php-pcre
Requires: php-spl

# Composer
Provides: php-composer(%{composer_vendor}/security-bundle) = %{version}
# Rename
Obsoletes: %{name}-securitybundle < %{version}
Provides:  %{name}-securitybundle = %{version}

%description security-bundle
%{summary}.

Configuration reference:
http://symfony.com/doc/2.8/reference/configuration/security.html

# ------------------------------------------------------------------------------

%package  twig-bundle

Summary:  Symfony Twig Bundle

# composer.json
Requires: php-composer(%{composer_vendor}/asset)           = %{version}
Requires: php-composer(%{composer_vendor}/http-foundation) = %{version}
Requires: php-composer(%{composer_vendor}/http-kernel)     = %{version}
Requires: php-composer(%{composer_vendor}/twig-bridge)     = %{version}
# phpcompatinfo (computed from version 2.8.6)
Requires: php-ctype
Requires: php-reflection
Requires: php-spl

# Composer
Provides: php-composer(%{composer_vendor}/twig-bundle) = %{version}
# Rename
Obsoletes: %{name}-twigbundle < %{version}
Provides:  %{name}-twigbundle = %{version}

%description twig-bundle
%{summary}

Configuration reference:
http://symfony.com/doc/2.8/reference/configuration/twig.html

# ------------------------------------------------------------------------------

%package  web-profiler-bundle

Summary:  Symfony WebProfiler Bundle

# composer.json
Requires: php-composer(%{composer_vendor}/http-kernel) = %{version}
Requires: php-composer(%{composer_vendor}/routing)     = %{version}
Requires: php-composer(%{composer_vendor}/twig-bridge) = %{version}
# phpcompatinfo (computed from version 2.8.6)
Requires: php-pcre
Requires: php-spl

# Composer
Provides: php-composer(%{composer_vendor}/web-profiler-bundle) = %{version}
# Rename
Obsoletes: %{name}-webprofilerbundle < %{version}
Provides:  %{name}-webprofilerbundle = %{version}

%description web-profiler-bundle
%{summary}

Configuration reference:
http://symfony.com/doc/2.8/reference/configuration/web_profiler.html

# ------------------------------------------------------------------------------

%package   asset

Summary:   Symfony Asset Component
URL:       http://symfony.com/doc/2.8/components/asset/index.html

# composer.json: optional
Requires:  php-composer(%{composer_vendor}/http-foundation) = %{version}
# phpcompatinfo (computed from version 2.8.6)
Requires:  php-hash
Requires:  php-spl

# Composer
Provides:  php-composer(%{composer_vendor}/asset) = %{version}

%description asset
The Asset component manages asset URLs.

# ------------------------------------------------------------------------------

%package   browser-kit

Summary:   Symfony BrowserKit Component

# composer.json
Requires:  php-composer(%{composer_vendor}/dom-crawler) = %{version}
# composer.json: optional
Requires:  php-composer(%{composer_vendor}/process)     = %{version}
# phpcompatinfo (computed from version 2.8.6)
Requires:  php-date
Requires:  php-pcre
Requires:  php-spl

# Composer
Provides:  php-composer(%{composer_vendor}/browser-kit) = %{version}
# PEAR
Provides:  php-pear(%{pear_channel}/BrowserKit) = %{version}
# Rename
Obsoletes: %{name}2-BrowserKit < %{version}
Provides:  %{name}2-BrowserKit = %{version}
Obsoletes: %{name}-browserkit  < %{version}
Provides:  %{name}-browserkit  = %{version}

%description browser-kit
BrowserKit simulates the behavior of a web browser.

The component only provide an abstract client and does not provide any
"default" backend for the HTTP layer.

# ------------------------------------------------------------------------------

%package   class-loader

Summary:   Symfony ClassLoader Component
URL:       http://symfony.com/doc/2.8/components/class_loader/index.html

Requires:  %{name}-common = %{version}-%{release}
# phpcompatinfo (computed from version 2.8.6)
Requires:  php-hash
Requires:  php-pcre
Requires:  php-reflection
Requires:  php-spl
Requires:  php-tokenizer

# Composer
Provides:  php-composer(%{composer_vendor}/class-loader) = %{version}
# PEAR
Provides:  php-pear(%{pear_channel}/ClassLoader) = %{version}
# Rename
Obsoletes: %{name}2-ClassLoader < %{version}
Provides:  %{name}2-ClassLoader = %{version}
Obsoletes: %{name}-classloader  < %{version}
Provides:  %{name}-classloader  = %{version}

%description class-loader
The ClassLoader Component loads your project classes automatically if they
follow some standard PHP conventions.

Whenever you use an undefined class, PHP uses the autoloading mechanism
to delegate the loading of a file defining the class. Symfony provides
a "universal" autoloader, which is able to load classes from files that
implement one of the following conventions:
* The technical interoperability standards [1] for PHP 5.3 namespaces
  and class names
* The PEAR naming convention [2] for classes

If your classes and the third-party libraries you use for your project follow
these standards, the Symfony autoloader is the only autoloader you will ever
need.

Optional:
* APC (php-pecl-apcu)
* XCache (php-xcache)

[1] http://symfony.com/PSR0
[2] http://pear.php.net/manual/en/standards.php

# ------------------------------------------------------------------------------

%package   config

Summary:   Symfony Config Component
URL:       http://symfony.com/doc/2.8/components/config/index.html

# composer.json
Requires:  php-composer(%{composer_vendor}/filesystem) = %{version}
# composer.json: optional
Requires:  php-composer(%{composer_vendor}/yaml)       = %{version}
# phpcompatinfo (computed from version 2.8.6)
Requires:  php-ctype
Requires:  php-dom
Requires:  php-json
Requires:  php-libxml
Requires:  php-pcre
Requires:  php-spl

# Composer
Provides:  php-composer(%{composer_vendor}/config) = %{version}
# PEAR
Provides:  php-pear(%{pear_channel}/Config) = %{version}
# Rename
Obsoletes: %{name}2-Config < %{version}
Provides:  %{name}2-Config = %{version}

%description config
The Config Component provides several classes to help you find, load, combine,
autofill and validate configuration values of any kind, whatever their source
may be (Yaml, XML, INI files, or for instance a database).

# ------------------------------------------------------------------------------

%package   console

Summary:   Symfony Console Component
URL:       http://symfony.com/doc/2.8/components/console/index.html

# composer.json: optional
Requires:  php-composer(%{composer_vendor}/event-dispatcher) =  %{version}
Requires:  php-composer(%{composer_vendor}/process)          =  %{version}
%if %{with_range_dependencies}
Requires:  (php-composer(psr/log) >= %{psr_log_min_ver} with php-composer(psr/log) < %{psr_log_max_ver})
%else
Requires:  php-composer(psr/log)                             >= %{psr_log_min_ver}
Requires:  php-composer(psr/log)                             <  %{psr_log_max_ver}
%endif
# phpcompatinfo (computed from version 2.8.6)
Requires:  php-date
Requires:  php-dom
Requires:  php-json
Requires:  php-mbstring
Requires:  php-pcre
Requires:  php-posix
Requires:  php-readline
Requires:  php-reflection
Requires:  php-spl

# Composer
Provides:  php-composer(%{composer_vendor}/console) = %{version}
# PEAR
Provides:  php-pear(%{pear_channel}/Console) = %{version}
# Rename
Obsoletes: %{name}2-Console < %{version}
Provides:  %{name}2-Console = %{version}

%description console
The Console component eases the creation of beautiful and testable command line
interfaces.

The Console component allows you to create command-line commands. Your console
commands can be used for any recurring task, such as cronjobs, imports, or
other batch jobs.

# ------------------------------------------------------------------------------

%package   css-selector

Summary:   Symfony CssSelector Component
URL:       http://symfony.com/doc/2.8/components/css_selector.html

Requires:  %{name}-common = %{version}-%{release}
# phpcompatinfo (computed from version 2.8.6)
Requires:  php-pcre

# Composer
Provides:  php-composer(%{composer_vendor}/css-selector) = %{version}
# PEAR
Provides:  php-pear(%{pear_channel}/CssSelector) = %{version}
# Rename
Obsoletes: %{name}2-CssSelector < %{version}
Provides:  %{name}2-CssSelector = %{version}
Obsoletes: %{name}-cssselector  < %{version}
Provides:  %{name}-cssselector  = %{version}

%description css-selector
The CssSelector Component converts CSS selectors to XPath expressions.

# ------------------------------------------------------------------------------

%package  debug

Summary:  Symfony Debug Component
URL:      http://symfony.com/doc/2.8/components/debug/index.html

Requires:  %{name}-common = %{version}-%{release}
# composer.json
%if %{with_range_dependencies}
Requires:  (php-composer(psr/log) >= %{psr_log_min_ver} with php-composer(psr/log) < %{psr_log_max_ver})
%else
Requires:  php-composer(psr/log) >= %{psr_log_min_ver}
Requires:  php-composer(psr/log) <  %{psr_log_max_ver}
%endif
# phpcompatinfo (computed from version 2.8.6)
Requires: php-pcre
Requires: php-reflection
Requires: php-spl

# Composer
Provides: php-composer(%{composer_vendor}/debug) = %{version}
# PEAR
Provides: php-pear(%{pear_channel}/Debug) = %{version}

%description debug
The Debug Component provides tools to ease debugging PHP code.

Optional:
* Xdebug (php-pecl-xdebug)

# ------------------------------------------------------------------------------

%package   dependency-injection

Summary:   Symfony DependencyInjection Component
URL:       http://symfony.com/doc/2.8/components/dependency_injection/index.html

# composer.json: optional
Requires:  php-composer(%{composer_vendor}/config)              = %{version}
Requires:  php-composer(%{composer_vendor}/yaml)                = %{version}
Requires:  php-composer(%{composer_vendor}/expression-language) = %{version}
# phpcompatinfo (computed from version 2.8.6)
Requires:  php-dom
Requires:  php-hash
Requires:  php-pcre
Requires:  php-reflection
Requires:  php-simplexml
Requires:  php-spl

# Composer
Provides:  php-composer(%{composer_vendor}/dependency-injection) = %{version}
# PEAR
Provides:  php-pear(%{pear_channel}/DependencyInjection) = %{version}
# Rename
Obsoletes: %{name}2-DependencyInjection < %{version}
Provides:  %{name}2-DependencyInjection = %{version}
Obsoletes: %{name}-dependencyinjection  < %{version}
Provides:  %{name}-dependencyinjection  = %{version}

%description dependency-injection
The Dependency Injection component allows you to standardize and centralize
the way objects are constructed in your application.

Optional:
* Symfony ProxyManager Bridge (php-%{composer_vendor}-proxy-manager-bridge)
      Generate service proxies to lazy load them.

# ------------------------------------------------------------------------------

%package   dom-crawler

Summary:   Symfony DomCrawler Component
URL:       http://symfony.com/doc/2.8/components/dom_crawler.html

# composer.json: optional
Requires:  php-composer(%{composer_vendor}/css-selector) = %{version}
# phpcompatinfo (computed from version 2.8.6)
Requires:  php-dom
Requires:  php-libxml
Requires:  php-mbstring
Requires:  php-pcre
Requires:  php-spl

# Composer
Provides:  php-composer(%{composer_vendor}/dom-crawler) = %{version}
# PEAR
Provides:  php-pear(%{pear_channel}/DomCrawler) = %{version}
# Rename
Obsoletes: %{name}2-DomCrawler < %{version}
Provides:  %{name}2-DomCrawler = %{version}
Obsoletes: %{name}-domcrawler  < %{version}
Provides:  %{name}-domcrawler  = %{version}

%description dom-crawler
The DomCrawler Component eases DOM navigation for HTML and XML documents.

# ------------------------------------------------------------------------------

%package   event-dispatcher

Summary:   Symfony EventDispatcher Component
URL:       http://symfony.com/doc/2.8/components/event_dispatcher/index.html

# composer.json: optional
Requires:  php-composer(%{composer_vendor}/dependency-injection) = %{version}
Requires:  php-composer(%{composer_vendor}/http-kernel)          = %{version}
# phpcompatinfo (computed from version 2.8.6)
Requires:  php-pcre
Requires:  php-reflection
Requires:  php-spl

# Composer
Provides:  php-composer(%{composer_vendor}/event-dispatcher) = %{version}
# PEAR
Provides:  php-pear(%{pear_channel}/EventDispatcher) = %{version}
# Rename
Obsoletes: %{name}2-EventDispatcher < %{version}
Provides:  %{name}2-EventDispatcher = %{version}
Obsoletes: %{name}-eventdispatcher  < %{version}
Provides:  %{name}-eventdispatcher  = %{version}

%description event-dispatcher
The Symfony Event Dispatcher component implements the Observer [1] pattern in
a simple and effective way to make all these things possible and to make your
projects truly extensible.

[1] http://en.wikipedia.org/wiki/Observer_pattern

# ------------------------------------------------------------------------------

%package   expression-language

Summary:   Symfony ExpressionLanguage Component
URL:       http://symfony.com/doc/2.8/components/expression_language/index.html

Requires:  %{name}-common = %{version}-%{release}
# phpcompatinfo (computed from version 2.8.6)
Requires:  php-ctype
Requires:  php-pcre
Requires:  php-spl

# Composer
Provides:  php-composer(%{composer_vendor}/expression-language) = %{version}
# PEAR
Provides:  php-pear(%{pear_channel}/ExpressionLanguage) = %{version}
# Rename
Obsoletes: %{name}-expressionlanguage < %{version}
Provides:  %{name}-expressionlanguage = %{version}

%description expression-language
The ExpressionLanguage component provides an engine that can compile and
evaluate expressions. An expression is a one-liner that returns a value
(mostly, but not limited to, Booleans).

# ------------------------------------------------------------------------------

%package   filesystem

Summary:   Symfony Filesystem Component
URL:       http://symfony.com/doc/2.8/components/filesystem/index.html

Requires:  %{name}-common = %{version}-%{release}
# phpcompatinfo (computed from version 2.8.6)
Requires:  php-ctype
Requires:  php-hash
Requires:  php-pcre
Requires:  php-posix
Requires:  php-spl

# Composer
Provides:  php-composer(%{composer_vendor}/filesystem) = %{version}
# PEAR
Provides:  php-pear(%{pear_channel}/Filesystem) = %{version}
# Rename
Obsoletes: %{name}2-Filesystem < %{version}
Provides:  %{name}2-Filesystem = %{version}

%description filesystem
The Filesystem component provides basic utilities for the filesystem.

# ------------------------------------------------------------------------------

%package   finder

Summary:   Symfony Finder Component
URL:       http://symfony.com/doc/2.8/components/finder.html

Requires:  %{name}-common = %{version}-%{release}
# phpcompatinfo (computed from version 2.8.6)
Requires:  php-date
Requires:  php-pcre
Requires:  php-spl

# Composer
Provides:  php-composer(%{composer_vendor}/finder) = %{version}
# PEAR
Provides:  php-pear(%{pear_channel}/Finder) = %{version}
# Rename
Obsoletes: %{name}2-Finder < %{version}
Provides:  %{name}2-Finder = %{version}

%description finder
The Finder Component finds files and directories via an intuitive fluent
interface.

# ------------------------------------------------------------------------------

%package   form

Summary:   Symfony Form Component
URL:       http://symfony.com/doc/2.8/components/form/index.html

# composer.json
Requires:  php-composer(%{composer_vendor}/event-dispatcher) = %{version}
Requires:  php-composer(%{composer_vendor}/intl)             = %{version}
Requires:  php-composer(%{composer_vendor}/options-resolver) = %{version}
Requires:  php-composer(%{composer_vendor}/property-access)  = %{version}
# composer.json: optional
Requires:  php-composer(%{composer_vendor}/security-csrf)    = %{version}
Requires:  php-composer(%{composer_vendor}/validator)        = %{version}
# phpcompatinfo (computed from version 2.8.6)
Requires:  php-ctype
Requires:  php-date
Requires:  php-hash
Requires:  php-intl
Requires:  php-mbstring
Requires:  php-pcre
Requires:  php-reflection
Requires:  php-session
Requires:  php-spl

# Composer
Provides:  php-composer(%{composer_vendor}/form) = %{version}
# PEAR
Provides:  php-pear(%{pear_channel}/Form) = %{version}
# Rename
Obsoletes: %{name}2-Form < %{version}
Provides:  %{name}2-Form = %{version}

%description form
Form provides tools for defining forms, rendering and mapping request data
to related models. Furthermore it provides integration with the Validation
component.

Optional:
* Symfony Framework Bundle (php-%{composer_vendor}-framework-bundle)
      For templating with PHP.
* Symfony Twig Bridge (php-%{composer_vendor}-twig-bridge)
      For templating with Twig.

# ------------------------------------------------------------------------------

%package   http-foundation

Summary:   Symfony HttpFoundation Component
URL:       http://symfony.com/doc/2.8/components/http_foundation/index.html

Requires:  %{name}-common = %{version}-%{release}
# composer.json
# phpcompatinfo (computed from version 2.8.6)
Requires:  php-date
Requires:  php-fileinfo
Requires:  php-filter
Requires:  php-hash
Requires:  php-intl
Requires:  php-json
Requires:  php-mbstring
Requires:  php-pcre
Requires:  php-pdo
Requires:  php-session
Requires:  php-sockets
Requires:  php-spl

# Composer
Provides:  php-composer(%{composer_vendor}/http-foundation) = %{version}
# PEAR
Provides:  php-pear(%{pear_channel}/HttpFoundation) = %{version}
# Rename
Obsoletes: %{name}2-HttpFoundation < %{version}
Provides:  %{name}2-HttpFoundation = %{version}
Obsoletes: %{name}-httpfoundation  < %{version}
Provides:  %{name}-httpfoundation  = %{version}

%description http-foundation
The HttpFoundation Component defines an object-oriented layer for the HTTP
specification.

In PHP, the request is represented by some global variables ($_GET, $_POST,
$_FILES, $_COOKIE, $_SESSION, ...) and the response is generated by some
functions (echo, header, setcookie, ...).

The Symfony HttpFoundation component replaces these default PHP global
variables and functions by an Object-Oriented layer.

Optional:
* Memcache (php-pecl-memcache)
* Memcached (php-pecl-memcached)
* Mongo (php-pecl-mongo)

# ------------------------------------------------------------------------------

%package   http-kernel

Summary:   Symfony HttpKernel Component
URL:       http://symfony.com/doc/2.8/components/http_kernel/index.html

# composer.json
Requires:  php-composer(%{composer_vendor}/debug)                =  %{version}
Requires:  php-composer(%{composer_vendor}/event-dispatcher)     =  %{version}
Requires:  php-composer(%{composer_vendor}/http-foundation)      =  %{version}
%if %{with_range_dependencies}
Requires:  (php-composer(psr/log) >= %{psr_log_min_ver} with php-composer(psr/log) < %{psr_log_max_ver})
%else
Requires:  php-composer(psr/log)                                 >= %{psr_log_min_ver}
Requires:  php-composer(psr/log)                                 <  %{psr_log_max_ver}
%endif
# composer.json: optional
Requires:  php-composer(%{composer_vendor}/browser-kit)          =  %{version}
Requires:  php-composer(%{composer_vendor}/class-loader)         =  %{version}
Requires:  php-composer(%{composer_vendor}/config)               =  %{version}
Requires:  php-composer(%{composer_vendor}/console)              =  %{version}
Requires:  php-composer(%{composer_vendor}/dependency-injection) =  %{version}
Requires:  php-composer(%{composer_vendor}/finder)               =  %{version}
Requires:  php-composer(%{composer_vendor}/var-dumper)           =  %{version}
# phpcompatinfo (computed from version 2.8.6)
Requires:  php-date
Requires:  php-hash
Requires:  php-pcre
Requires:  php-pdo
Requires:  php-reflection
Requires:  php-session
Requires:  php-spl
Requires:  php-sqlite3
Requires:  php-tokenizer

# Composer
Provides:  php-composer(%{composer_vendor}/http-kernel) = %{version}
# PEAR
Provides:  php-pear(%{pear_channel}/HttpKernel) = %{version}
# Rename
Obsoletes: %{name}2-HttpKernel < %{version}
Provides:  %{name}2-HttpKernel = %{version}
Obsoletes: %{name}-httpkernel  < %{version}
Provides:  %{name}-httpkernel  = %{version}

%description http-kernel
The HttpKernel Component provides a structured process for converting a Request
into a Response by making use of the event dispatcher. It's flexible enough to
create a full-stack framework (Symfony), a micro-framework (Silex) or an
advanced CMS system (Drupal).

Configuration reference:
http://symfony.com/doc/2.8/reference/configuration/kernel.html

Optional:
* APC (php-pecl-apcu)
* Memcache (php-pecl-memcache)
* Memcached (php-pecl-memcached)
* Mongo (php-pecl-mongo)
* Redis (php-pecl-redis)
* Zend OPcache (php-opcache)

# ------------------------------------------------------------------------------

%package   intl

Summary:   Symfony Intl Component
URL:       http://symfony.com/doc/2.8/components/intl.html

Requires:  %{name}-common = %{version}-%{release}
#composer.json
# composer.json: optional
Requires:  php-intl
# phpcompatinfo (computed from version 2.8.6)
Requires:  php-ctype
Requires:  php-date
Requires:  php-json
Requires:  php-pcre
Requires:  php-reflection
Requires:  php-simplexml
Requires:  php-spl

# Composer
Provides:  php-composer(%{composer_vendor}/intl) = %{version}
# PEAR
Provides:  php-pear(%{pear_channel}/Intl) = %{version}
# Rename
Obsoletes: %{name}2-Intl < %{version}
Provides:  %{name}2-Intl = %{version}
# ICU
Obsoletes: php-symfony-icu

%description intl
A PHP replacement layer for the C intl extension [1] that also provides access
to the localization data of the ICU library [2].

[1] http://www.php.net/manual/en/book.intl.php
[2] http://site.icu-project.org/

# ------------------------------------------------------------------------------

%package   ldap

Summary:   Symfony LDAP Component

Requires:  %{name}-common = %{version}-%{release}
# composer.json
Requires:  php-ldap
# phpcompatinfo (computed from version 2.8.6)
Requires:  php-spl

# Composer
Provides:  php-composer(%{composer_vendor}/ldap) = %{version}

%description ldap
An abstraction in front of PHP's LDAP functions.

# ------------------------------------------------------------------------------

%package   locale

Summary:   Symfony Locale Component
URL:       http://symfony.com/doc/2.2/components/locale.html

# composer.json
Requires:  php-composer(%{composer_vendor}/intl) = %{version}
# phpcompatinfo (computed from version 2.8.6)
Requires:  php-intl

# Composer
Provides:  php-composer(%{composer_vendor}/locale) = %{version}
# PEAR
Provides:  php-pear(%{pear_channel}/Locale) = %{version}
# Rename
Obsoletes: %{name}2-Locale < %{version}
Provides:  %{name}2-Locale = %{version}

%description locale
Locale provides fallback code to handle cases when the intl extension is
missing.

The Locale component is deprecated since version 2.3 and will be removed in
Symfony 3.0. You should use the more capable Intl component instead.

# ------------------------------------------------------------------------------

%package   options-resolver

Summary:   Symfony OptionsResolver Component
URL:       http://symfony.com/doc/2.8/components/options_resolver.html

Requires:  %{name}-common = %{version}-%{release}
# phpcompatinfo (computed from version 2.8.6)
Requires:  php-reflection
Requires:  php-spl

# Composer
Provides:  php-composer(%{composer_vendor}/options-resolver) = %{version}
# PEAR
Provides:  php-pear(%{pear_channel}/OptionsResolver) = %{version}
# Rename
Obsoletes: %{name}2-OptionsResolver < %{version}
Provides:  %{name}2-OptionsResolver = %{version}
Obsoletes: %{name}-optionsresolver  < %{version}
Provides:  %{name}-optionsresolver  = %{version}

%description options-resolver
The OptionsResolver Component helps you configure objects with option arrays.
It supports default values, option constraints and lazy options.

# ------------------------------------------------------------------------------

%package   process

Summary:   Symfony Process Component
URL:       http://symfony.com/doc/2.8/components/process.html

Requires:  %{name}-common = %{version}-%{release}
# phpcompatinfo (computed from version 2.8.6)
Requires:  php-pcre
Requires:  php-posix
Requires:  php-spl

# Composer
Provides:  php-composer(%{composer_vendor}/process) = %{version}
# PEAR
Provides:  php-pear(%{pear_channel}/Process) = %{version}
# Rename
Obsoletes: %{name}2-Process < %{version}
Provides:  %{name}2-Process = %{version}

%description process
The Process component executes commands in sub-processes.

# ------------------------------------------------------------------------------

%package   property-access

Summary:   Symfony PropertyAccess Component
URL:       http://symfony.com/doc/2.8/components/property_access/index.html

Requires:  %{name}-common = %{version}-%{release}
# phpcompatinfo (computed from version 2.8.6)
Requires:  php-ctype
Requires:  php-pcre
Requires:  php-reflection
Requires:  php-spl

# Composer
Provides:  php-composer(%{composer_vendor}/property-access) = %{version}
# PEAR
Provides:  php-pear(%{pear_channel}/PropertyAccess) = %{version}
# Rename
Obsoletes: %{name}2-PropertyAccess < %{version}
Provides:  %{name}2-PropertyAccess = %{version}
Obsoletes: %{name}-propertyaccess  < %{version}
Provides:  %{name}-propertyaccess  = %{version}

%description property-access
The PropertyAccess component provides function to read and write from/to an
object or array using a simple string notation.

# ------------------------------------------------------------------------------

%package  property-info

Summary:  Symfony Property Info Component

# composer.json: optional
Requires: php-composer(%{composer_vendor}/doctrine-bridge) =  %{version}
Requires: php-composer(%{composer_vendor}/serializer)      =  %{version}
%if %{with_range_dependencies}
Requires: (php-composer(phpdocumentor/reflection) >= %{phpdocumentor_reflection_min_ver} with php-composer(phpdocumentor/reflection) < %{phpdocumentor_reflection_max_ver})
%else
Requires: php-composer(phpdocumentor/reflection)           <  %{phpdocumentor_reflection_max_ver}
Requires: php-composer(phpdocumentor/reflection)           >= %{phpdocumentor_reflection_min_ver}
%endif
# phpcompatinfo (computed from version 2.8.6)
Requires: php-pcre
Requires: php-reflection
Requires: php-spl

# Composer
Provides: php-composer(%{composer_vendor}/property-info) = %{version}

%description property-info
PropertyInfo extracts information about PHP class' properties using metadata of
popular sources.

# ------------------------------------------------------------------------------

%package   routing

Summary:   Symfony Routing Component
URL:       http://symfony.com/doc/2.8/components/routing/index.html

# composer.json: optional
Requires:  php-composer(%{composer_vendor}/config)               =  %{version}
Requires:  php-composer(%{composer_vendor}/dependency-injection) =  %{version}
Requires:  php-composer(%{composer_vendor}/expression-language)  =  %{version}
Requires:  php-composer(%{composer_vendor}/http-foundation)      =  %{version}
Requires:  php-composer(%{composer_vendor}/yaml)                 =  %{version}
%if %{with_range_dependencies}
Requires:  (php-composer(doctrine/annotations) >= %{doctrine_annotations_min_ver} with php-composer(doctrine/annotations) < %{doctrine_annotations_max_ver})
%else
Requires:  php-composer(doctrine/annotations)                    <  %{doctrine_annotations_max_ver}
Requires:  php-composer(doctrine/annotations)                    >= %{doctrine_annotations_min_ver}
%endif
# phpcompatinfo (computed from version 2.8.6)
Requires:  php-pcre
Requires:  php-reflection
Requires:  php-spl
Requires:  php-tokenizer

# Composer
Provides:  php-composer(%{composer_vendor}/routing) = %{version}
# PEAR
Provides:  php-pear(%{pear_channel}/Routing) = %{version}
# Rename
Obsoletes: %{name}2-Routing < %{version}
Provides:  %{name}2-Routing = %{version}

%description routing
The Routing Component maps an HTTP request to a set of configuration variables.

# ------------------------------------------------------------------------------

%package   security

Summary:   Symfony Security Component
URL:       http://symfony.com/doc/2.8/components/security/index.html

# composer.json
Requires:  php-composer(%{composer_vendor}/event-dispatcher)    =  %{version}
Requires:  php-composer(%{composer_vendor}/http-foundation)     =  %{version}
Requires:  php-composer(%{composer_vendor}/http-kernel)         =  %{version}
Requires:  php-composer(%{composer_vendor}/property-access)     =  %{version}
%if %{with_range_dependencies}
Requires:  (php-composer(symfony/polyfill-util) >= %{symfony_polyfill_min_ver} with php-composer(symfony/polyfill-util) < %{symfony_polyfill_max_ver})
Requires:  (php-composer(symfony/security-acl) >= %{symfony_security_acl_min_ver} with php-composer(symfony/security-acl) < %{symfony_security_acl_max_ver})
%else
Requires:  php-composer(symfony/polyfill-util)                  <  %{symfony_polyfill_max_ver}
Requires:  php-composer(symfony/polyfill-util)                  >= %{symfony_polyfill_min_ver}
Requires:  php-composer(symfony/security-acl)                   <  %{symfony_security_acl_max_ver}
Requires:  php-composer(symfony/security-acl)                   >= %{symfony_security_acl_min_ver}
%endif
# composer.json: optional
Requires:  php-composer(%{composer_vendor}/expression-language) =  %{version}
Requires:  php-composer(%{composer_vendor}/form)                =  %{version}
Requires:  php-composer(%{composer_vendor}/ldap)                =  %{version}
Requires:  php-composer(%{composer_vendor}/routing)             =  %{version}
Requires:  php-composer(%{composer_vendor}/validator)           =  %{version}
# phpcompatinfo (computed from version 2.8.6)
Requires:  php-ctype
Requires:  php-date
Requires:  php-hash
Requires:  php-json
Requires:  php-ldap
Requires:  php-pcre
Requires:  php-reflection
Requires:  php-session
Requires:  php-spl

# Composer
Provides: php-composer(%{composer_vendor}/security-core)  = %{version}
Provides: php-composer(%{composer_vendor}/security-csrf)  = %{version}
Provides: php-composer(%{composer_vendor}/security-guard) = %{version}
Provides: php-composer(%{composer_vendor}/security-http)  = %{version}
Provides: php-composer(%{composer_vendor}/security)       = %{version}
# Composer sub-packages
Provides:  %{name}-security-core  = %{version}-%{release}
Provides:  %{name}-security-csrf  = %{version}-%{release}
Provides:  %{name}-security-guard = %{version}-%{release}
Provides:  %{name}-security-http  = %{version}-%{release}
# PEAR
Provides:  php-pear(%{pear_channel}/Security) = %{version}
# Rename
Obsoletes: %{name}2-Security < %{version}
Provides:  %{name}2-Security = %{version}

%description security
The Security Component provides a complete security system for your web
application. It ships with facilities for authenticating using HTTP basic
or digest authentication, interactive form login or X.509 certificate login,
but also allows you to implement your own authentication strategies.
Furthermore, the component provides ways to authorize authenticated users
based on their roles, and it contains an advanced ACL system.

Optional:
* Symfony LDAP Component (php-%{composer_vendor}-ldap)
      For using the LDAP user and authentication providers.

# ------------------------------------------------------------------------------

%package   serializer

Summary:   Symfony Serializer Component
URL:       http://symfony.com/doc/2.8/components/serializer.html

# composer.json
# composer.json: optional
Requires:  php-composer(%{composer_vendor}/config)          =  %{version}
Requires:  php-composer(%{composer_vendor}/property-access) =  %{version}
Requires:  php-composer(%{composer_vendor}/yaml)            =  %{version}
%if %{with_range_dependencies}
Requires:  (php-composer(doctrine/annotations) >= %{doctrine_annotations_min_ver} with php-composer(doctrine/annotations) < %{doctrine_annotations_max_ver})
Requires:  (php-composer(doctrine/cache) >= %{doctrine_cache_min_ver} with php-composer(doctrine/cache) < %{doctrine_cache_max_ver})
%else
Requires:  php-composer(doctrine/annotations)               <  %{doctrine_annotations_max_ver}
Requires:  php-composer(doctrine/annotations)               >= %{doctrine_annotations_min_ver}
Requires:  php-composer(doctrine/cache)                     <  %{doctrine_cache_max_ver}
Requires:  php-composer(doctrine/cache)                     >= %{doctrine_cache_min_ver}
%endif
# phpcompatinfo (computed from version 2.8.6)
Requires:  php-ctype
Requires:  php-dom
Requires:  php-json
Requires:  php-libxml
Requires:  php-pcre
Requires:  php-reflection
Requires:  php-simplexml
Requires:  php-spl

# Composer
Provides:  php-composer(%{composer_vendor}/serializer) = %{version}
# PEAR
Provides:  php-pear(%{pear_channel}/Serializer) = %{version}
# Rename
Obsoletes: %{name}2-Serializer < %{version}
Provides:  %{name}2-Serializer = %{version}

%description serializer
The Serializer Component is meant to be used to turn objects into a specific
format (XML, JSON, Yaml, ...) and the other way around.

# ------------------------------------------------------------------------------

%package  stopwatch

Summary:  Symfony Stopwatch Component
URL:      http://symfony.com/doc/2.8/components/stopwatch.html

Requires: %{name}-common = %{version}-%{release}
# phpcompatinfo (computed from version 2.8.6)
Requires: php-spl

# Composer
Provides: php-composer(%{composer_vendor}/stopwatch) = %{version}
# PEAR
Provides: php-pear(%{pear_channel}/Stopwatch) = %{version}

%description stopwatch
Stopwatch component provides a way to profile code.

# ------------------------------------------------------------------------------

%package   templating

Summary:   Symfony Templating Component
URL:       http://symfony.com/doc/2.8/components/templating/index.html

Requires:  %{name}-common        =  %{version}-%{release}
# composer.json: optional
%if %{with_range_dependencies}
Requires:  (php-composer(psr/log) >= %{psr_log_min_ver} with php-composer(psr/log) < %{psr_log_max_ver})
%else
Requires:  php-composer(psr/log) >= %{psr_log_min_ver}
Requires:  php-composer(psr/log) <  %{psr_log_max_ver}
%endif
# phpcompatinfo (computed from version 2.8.6)
Requires:  php-ctype
Requires:  php-hash
Requires:  php-iconv
Requires:  php-pcre
Requires:  php-spl

# Composer
Provides:  php-composer(%{composer_vendor}/templating) = %{version}
# PEAR
Provides:  php-pear(%{pear_channel}/Templating) = %{version}
# Rename
Obsoletes: %{name}2-Templating < %{version}
Provides:  %{name}2-Templating = %{version}

%description templating
Templating provides all the tools needed to build any kind of template system.

It provides an infrastructure to load template files and optionally monitor
them for changes. It also provides a concrete template engine implementation
using PHP with additional tools for escaping and separating templates into
blocks and layouts.

# ------------------------------------------------------------------------------

%package   translation

Summary:   Symfony Translation Component
URL:       http://symfony.com/doc/2.8/components/translation/index.html

# composer.json: optional
Requires:  php-composer(%{composer_vendor}/config) =  %{version}
Requires:  php-composer(%{composer_vendor}/yaml)   =  %{version}
%if %{with_range_dependencies}
Requires:  (php-composer(psr/log) >= %{psr_log_min_ver} with php-composer(psr/log) < %{psr_log_max_ver})
%else
Requires:  php-composer(psr/log)                   >= %{psr_log_min_ver}
Requires:  php-composer(psr/log)                   <  %{psr_log_max_ver}
%endif
# phpcompatinfo (computed from version 2.8.6)
Requires:  php-dom
Requires:  php-intl
Requires:  php-json
Requires:  php-libxml
Requires:  php-mbstring
Requires:  php-pcre
Requires:  php-simplexml
Requires:  php-spl

# Composer
Provides:  php-composer(%{composer_vendor}/translation) = %{version}
# PEAR
Provides:  php-pear(%{pear_channel}/Translation) = %{version}
# Rename
Obsoletes: %{name}2-Translation < %{version}
Provides:  %{name}2-Translation = %{version}

%description translation
Translation provides tools for loading translation files and generating
translated strings from these including support for pluralization.

# ------------------------------------------------------------------------------

%package   validator

Summary:   Symfony Validator Component

# composer.json
Requires:  php-composer(%{composer_vendor}/translation)         =  %{version}
# composer.json: optional
Requires:  php-composer(%{composer_vendor}/config)              =  %{version}
Requires:  php-composer(%{composer_vendor}/expression-language) =  %{version}
Requires:  php-composer(%{composer_vendor}/http-foundation)     =  %{version}
Requires:  php-composer(%{composer_vendor}/intl)                =  %{version}
Requires:  php-composer(%{composer_vendor}/property-access)     =  %{version}
Requires:  php-composer(%{composer_vendor}/yaml)                =  %{version}
%if %{with_range_dependencies}
Requires:  (php-composer(doctrine/annotations) >= %{doctrine_annotations_min_ver} with php-composer(doctrine/annotations) < %{doctrine_annotations_max_ver})
Requires:  (php-composer(doctrine/cache) >= %{doctrine_cache_min_ver} with php-composer(doctrine/cache) < %{doctrine_cache_max_ver})
Requires:  (php-composer(egulias/email-validator) >= %{email_validator_min_ver} with php-composer(egulias/email-validator) < %{email_validator_max_ver})
%else
Requires:  php-composer(doctrine/annotations)                   <  %{doctrine_annotations_max_ver}
Requires:  php-composer(doctrine/annotations)                   >= %{doctrine_annotations_min_ver}
Requires:  php-composer(doctrine/cache)                         <  %{doctrine_cache_max_ver}
Requires:  php-composer(doctrine/cache)                         >= %{doctrine_cache_min_ver}
Requires:  php-composer(egulias/email-validator)                <  %{email_validator_max_ver}
Requires:  php-composer(egulias/email-validator)                >= %{email_validator_min_ver}
%endif
# phpcompatinfo (computed from version 2.8.6)
Requires:  php-ctype
Requires:  php-date
Requires:  php-filter
Requires:  php-iconv
Requires:  php-intl
Requires:  php-json
Requires:  php-pcre
Requires:  php-reflection
Requires:  php-simplexml
Requires:  php-spl

# Composer
Provides:  php-composer(%{composer_vendor}/validator) = %{version}
# PEAR
Provides:  php-pear(%{pear_channel}/Validator) = %{version}
# Rename
Obsoletes: %{name}2-Validator < %{version}
Provides:  %{name}2-Validator = %{version}

%description validator
This component is based on the JSR-303 Bean Validation specification and
enables specifying validation rules for classes using XML, YAML, PHP or
annotations, which can then be checked against instances of these classes.

Optional:
* APC (php-pecl-apcu)

# ------------------------------------------------------------------------------

%package  var-dumper

Summary:  Symfony mechanism for exploring and dumping PHP variables
URL:      http://symfony.com/doc/2.8/components/var_dumper/index.html

Requires: %{name}-common = %{version}-%{release}
# composer.json: optional
# ext-symfony_debug
# phpcompatinfo (computed from version 2.8.6)
Requires: php-curl
Requires: php-date
Requires: php-dom
Requires: php-gd
Requires: php-iconv
Requires: php-json
Requires: php-mbstring
Requires: php-pcre
Requires: php-posix
Requires: php-reflection
Requires: php-spl
Requires: php-xml

# Composer
Provides: php-composer(%{composer_vendor}/var-dumper) = %{version}

%description var-dumper
This component provides a mechanism that allows exploring then dumping any PHP
variable.

It handles scalars, objects and resources properly, taking hard and soft
references into account. More than being immune to infinite recursion problems,
it allows dumping where references link to each other. It explores recursive
structures using a breadth-first algorithm.

The component exposes all the parts involved in the different steps of cloning
then dumping a PHP variable, while applying size limits and having specialized
output formats and methods.

Optional:
* AMQP (php-pecl-amqp)
* MySQL (php-mysql)
      Required for
      Symfony\Component\VarDumper\Caster\ResourceCaster::castMysqlLink()

# ------------------------------------------------------------------------------

%package   yaml

Summary:   Symfony Yaml Component
URL:       http://symfony.com/doc/2.8/components/yaml/index.html

Requires:  %{name}-common = %{version}-%{release}
# phpcompatinfo (computed from version 2.8.6)
Requires:  php-ctype
Requires:  php-date
Requires:  php-json
Requires:  php-mbstring
Requires:  php-pcre
Requires:  php-spl

# Composer
Provides:  php-composer(%{composer_vendor}/yaml) = %{version}
# PEAR
Provides:  php-pear(%{pear_channel}/Yaml) = %{version}
# Rename
Obsoletes: %{name}2-Yaml < %{version}
Provides:  %{name}2-Yaml = %{version}

%description yaml
The YAML Component loads and dumps YAML files.

# ##############################################################################


%prep
%setup -qn %{github_name}-%{github_commit}

: Remove unnecessary files
find src -name '.git*' -delete -print

: Remove unwanted components
rm -r src/Symfony/Bridge/Propel1

: Create autoloaders
cat << 'AUTOLOAD' | tee src/Symfony/Component/autoload.php
<?php
/**
 * Autoloader for all Symfony components and their dependencies.
 *
 * Created by %{name}-%{version}-%{release}
 *
 * @return \Symfony\Component\ClassLoader\ClassLoader
 */

if (!isset($fedoraClassLoader) || !($fedoraClassLoader instanceof \Symfony\Component\ClassLoader\ClassLoader)) {
    if (!class_exists('Symfony\\Component\\ClassLoader\\ClassLoader', false)) {
        require_once __DIR__ . '/ClassLoader/ClassLoader.php';
    }

    $fedoraClassLoader = new \Symfony\Component\ClassLoader\ClassLoader();
    $fedoraClassLoader->register();
}
$fedoraClassLoader->addPrefix('Symfony\\Component\\', dirname(dirname(__DIR__)));

// Optional dependency
foreach (array(
    '%{phpdir}/random_compat/autoload.php',
) as $dependencyAutoloader) {
    if (file_exists($dependencyAutoloader)) {
        require_once $dependencyAutoloader;
    }
}

return $fedoraClassLoader;
AUTOLOAD

cat << 'AUTOLOAD' | tee src/Symfony/autoload.php
<?php
/**
 * Autoloader for all Symfony bridges/bundles/components and their dependencies.
 *
 * Created by %{name}-%{version}-%{release}
 *
 * Note: This autoloader does not do any registration with the Doctrine
 * annotation registry (i.e. \Doctrine\Common\Annotations\AnnotationRegistry).
 *
 * @return \Symfony\Component\ClassLoader\ClassLoader
 */

require_once __DIR__ . '/Component/autoload.php';

if (!isset($fedoraClassLoader) || !($fedoraClassLoader instanceof \Symfony\Component\ClassLoader\ClassLoader)) {
    if (!class_exists('Symfony\\Component\\ClassLoader\\ClassLoader', false)) {
        require_once __DIR__ . '/ClassLoader/ClassLoader.php';
    }

    $fedoraClassLoader = new \Symfony\Component\ClassLoader\ClassLoader();
    $fedoraClassLoader->register();
}
$fedoraClassLoader->addPrefix('Symfony\\', dirname(__DIR__));

// Dependency autoloaders
foreach (array(
    '%{phpdir}/Doctrine/Bundle/DoctrineBundle/autoload.php',
    '%{phpdir}/Doctrine/Common/Annotations/autoload.php',
    '%{phpdir}/Doctrine/Common/autoload.php',
    '%{phpdir}/Doctrine/Common/Cache/autoload.php',
    '%{phpdir}/Doctrine/Common/DataFixtures/autoload.php',
    '%{phpdir}/Doctrine/DBAL/autoload.php',
    '%{phpdir}/Doctrine/ORM/autoload.php',
    '%{phpdir}/Egulias/EmailValidator/autoload.php',
    '%{phpdir}/Monolog/autoload.php',
    '%{phpdir}/ProxyManager/autoload.php',
    '%{phpdir}/Psr/Log/autoload.php',
    '%{phpdir}/Swift/swift_required.php',
    '%{phpdir}/Symfony/Polyfill/autoload.php',
    '%{phpdir}/Symfony/Security/Acl/autoload.php',
) as $dependencyAutoloader) {
    if (file_exists($dependencyAutoloader)) {
        require_once $dependencyAutoloader;
    }
}
if (file_exists($dep='%{phpdir}/phpDocumentor/Reflection1/autoload.php')) {
    require_once $dep;
} else if (file_exists($dep='%{phpdir}/phpDocumentor/Reflection/autoload.php')) {
    require_once $dep;
}
if (file_exists($dep='%{phpdir}/Twig2/autoload.php')) {
    require_once $dep;
} else if (file_exists($dep='%{phpdir}/Twig/autoload.php')) {
    require_once $dep;
}

return $fedoraClassLoader;
AUTOLOAD

: Create autoloader softlinks for each bridge/bundle/component
for PKG in src/Symfony/Component/*
do
  if [ -d $PKG ]; then
    ln -s ../autoload.php $PKG/autoload.php
    # PEAR compat
    ln -s ../autoload.php $PKG/autoloader.php
  fi
done
for PKG in src/Symfony/{Bridge,Bundle}/*
do
    ln -s ../../autoload.php $PKG/autoload.php
done


%build
# Empty build section, nothing required


%install
mkdir -p %{buildroot}%{symfony_dir}
cp -rp src/Symfony/* %{buildroot}%{symfony_dir}/

# Symlink main package docs to common sub-package docs
mkdir -p %{buildroot}%{_docdir}
%if 0%{?fedora} >= 20 || 0%{?rhel} >= 8
ln -s %{name}-common %{buildroot}%{_docdir}/%{name}
%else
ln -s %{name}-common-%{version} %{buildroot}%{_docdir}/%{name}-%{version}
%endif


%check
%if %{with_tests}
: Ensure TZ is set
cp -pf %{_sysconfdir}/php.ini .
echo "date.timezone=Europe/Paris" >> php.ini
export PHPRC=$PWD/php.ini
export RPM_SYMFONY_TREE=%{buildroot}%{phpdir}/Symfony

: Modify PHPUnit config
sed 's#./src#%{buildroot}%{phpdir}#' phpunit.xml.dist > phpunit.xml

: Create tests bootstrap
cat << 'BOOTSTRAP' | tee bootstrap.php
<?php

require_once '%{buildroot}%{phpdir}/Symfony/autoload.php';
require_once '%{buildroot}%{phpdir}/Symfony/Bridge/PhpUnit/bootstrap.php';
require_once '%{buildroot}%{phpdir}/Symfony/Component/VarDumper/Resources/functions/dump.php';
BOOTSTRAP

: Run tests
RET=0
for PKG in %{buildroot}%{phpdir}/Symfony/*/*; do
  if [ "$(basename $PKG)" = "PhpUnit" ]; then
    continue
  elif [ "$(basename $PKG)" = "Debug" ]; then
    continue
  elif [ -d $PKG ]; then
    echo -e "\n>>>>>>>>>>>>>>>>>>>>>>> ${PKG}\n"
    %{_bindir}/php -d serialize_precision=14 -d include_path=.:%{buildroot}%{phpdir}:%{phpdir} \
    %{_bindir}/phpunit \
        --exclude-group benchmark,intl-data,network,tty \
        --bootstrap bootstrap.php \
        $PKG || RET=1
  fi
done
: ignore test suite results
%else
: Tests skipped
%endif


%{!?_licensedir:%global license %%doc}

%files
%if 0%{?fedora} >= 20 || 0%{?rhel} >= 8
%doc %{_docdir}/%{name}
%else
%doc %{_docdir}/%{name}-%{version}
%endif


# ##############################################################################

%files common

%doc *.md composer.json
%license LICENSE

%dir %{symfony_dir}
     %{symfony_dir}/autoload.php
%dir %{symfony_dir}/Bridge
%dir %{symfony_dir}/Bundle
%dir %{symfony_dir}/Component
     %{symfony_dir}/Component/autoload.php

# ------------------------------------------------------------------------------

%files doctrine-bridge

%license src/Symfony/Bridge/Doctrine/LICENSE
%doc src/Symfony/Bridge/Doctrine/*.md
%doc src/Symfony/Bridge/Doctrine/composer.json

%{symfony_dir}/Bridge/Doctrine
%exclude %{symfony_dir}/Bridge/Doctrine/LICENSE
%exclude %{symfony_dir}/Bridge/Doctrine/*.md
%exclude %{symfony_dir}/Bridge/Doctrine/composer.json
%exclude %{symfony_dir}/Bridge/Doctrine/phpunit.*
%exclude %{symfony_dir}/Bridge/Doctrine/Tests

# ------------------------------------------------------------------------------

%files monolog-bridge

%license src/Symfony/Bridge/Monolog/LICENSE
%doc src/Symfony/Bridge/Monolog/*.md
%doc src/Symfony/Bridge/Monolog/composer.json

%{symfony_dir}/Bridge/Monolog
%exclude %{symfony_dir}/Bridge/Monolog/LICENSE
%exclude %{symfony_dir}/Bridge/Monolog/*.md
%exclude %{symfony_dir}/Bridge/Monolog/composer.json
%exclude %{symfony_dir}/Bridge/Monolog/phpunit.*
%exclude %{symfony_dir}/Bridge/Monolog/Tests

# ------------------------------------------------------------------------------

%files phpunit-bridge

%license src/Symfony/Bridge/PhpUnit/LICENSE
%doc src/Symfony/Bridge/PhpUnit/*.md
%doc src/Symfony/Bridge/PhpUnit/composer.json

%{symfony_dir}/Bridge/PhpUnit
%exclude %{symfony_dir}/Bridge/PhpUnit/LICENSE
%exclude %{symfony_dir}/Bridge/PhpUnit/*.md
%exclude %{symfony_dir}/Bridge/PhpUnit/composer.json
%exclude %{symfony_dir}/Bridge/PhpUnit/phpunit.*
%exclude %{symfony_dir}/Bridge/PhpUnit/Tests

# ------------------------------------------------------------------------------

%files proxy-manager-bridge

%license src/Symfony/Bridge/ProxyManager/LICENSE
%doc src/Symfony/Bridge/ProxyManager/*.md
%doc src/Symfony/Bridge/ProxyManager/composer.json

%{symfony_dir}/Bridge/ProxyManager
%exclude %{symfony_dir}/Bridge/ProxyManager/LICENSE
%exclude %{symfony_dir}/Bridge/ProxyManager/*.md
%exclude %{symfony_dir}/Bridge/ProxyManager/composer.json
%exclude %{symfony_dir}/Bridge/ProxyManager/phpunit.*
%exclude %{symfony_dir}/Bridge/ProxyManager/Tests

# ------------------------------------------------------------------------------

%files swiftmailer-bridge

%license src/Symfony/Bridge/Swiftmailer/LICENSE
%doc src/Symfony/Bridge/Swiftmailer/*.md
%doc src/Symfony/Bridge/Swiftmailer/composer.json

%{symfony_dir}/Bridge/Swiftmailer
%exclude %{symfony_dir}/Bridge/Swiftmailer/LICENSE
%exclude %{symfony_dir}/Bridge/Swiftmailer/*.md
%exclude %{symfony_dir}/Bridge/Swiftmailer/composer.json
#%%exclude %%{symfony_dir}/Bridge/Swiftmailer/phpunit.*
#%%exclude %%{symfony_dir}/Bridge/Swiftmailer/Tests

# ------------------------------------------------------------------------------

%files twig-bridge

%license src/Symfony/Bridge/Twig/LICENSE
%doc src/Symfony/Bridge/Twig/*.md
%doc src/Symfony/Bridge/Twig/composer.json

%{symfony_dir}/Bridge/Twig
%exclude %{symfony_dir}/Bridge/Twig/LICENSE
%exclude %{symfony_dir}/Bridge/Twig/*.md
%exclude %{symfony_dir}/Bridge/Twig/composer.json
%exclude %{symfony_dir}/Bridge/Twig/phpunit.*
%exclude %{symfony_dir}/Bridge/Twig/Tests

# ------------------------------------------------------------------------------

%files debug-bundle

#%%doc src/Symfony/Bundle/DebugBundle/*.md
%doc src/Symfony/Bundle/DebugBundle/composer.json
%license src/Symfony/Bundle/DebugBundle/LICENSE

%{symfony_dir}/Bundle/DebugBundle
#%%exclude %%{symfony_dir}/Bundle/DebugBundle/*.md
%exclude %{symfony_dir}/Bundle/DebugBundle/composer.json
%exclude %{symfony_dir}/Bundle/DebugBundle/phpunit.*
%exclude %{symfony_dir}/Bundle/DebugBundle/Tests
%exclude %{symfony_dir}/Bundle/DebugBundle/LICENSE

# ------------------------------------------------------------------------------

%files framework-bundle

%doc src/Symfony/Bundle/FrameworkBundle/*.md
%doc src/Symfony/Bundle/FrameworkBundle/composer.json
%license src/Symfony/Bundle/FrameworkBundle/LICENSE

%{symfony_dir}/Bundle/FrameworkBundle
%exclude %{symfony_dir}/Bundle/FrameworkBundle/*.md
%exclude %{symfony_dir}/Bundle/FrameworkBundle/composer.json
%exclude %{symfony_dir}/Bundle/FrameworkBundle/phpunit.*
%exclude %{symfony_dir}/Bundle/FrameworkBundle/Tests
%exclude %{symfony_dir}/Bundle/FrameworkBundle/LICENSE

# ------------------------------------------------------------------------------

%files security-bundle

%doc src/Symfony/Bundle/SecurityBundle/*.md
%doc src/Symfony/Bundle/SecurityBundle/composer.json
%license src/Symfony/Bundle/SecurityBundle/LICENSE

%{symfony_dir}/Bundle/SecurityBundle
%exclude %{symfony_dir}/Bundle/SecurityBundle/*.md
%exclude %{symfony_dir}/Bundle/SecurityBundle/composer.json
%exclude %{symfony_dir}/Bundle/SecurityBundle/phpunit.*
%exclude %{symfony_dir}/Bundle/SecurityBundle/Tests
%exclude %{symfony_dir}/Bundle/SecurityBundle/LICENSE

# ------------------------------------------------------------------------------

%files twig-bundle

%doc src/Symfony/Bundle/TwigBundle/*.md
%doc src/Symfony/Bundle/TwigBundle/composer.json
%license src/Symfony/Bundle/TwigBundle/LICENSE

%{symfony_dir}/Bundle/TwigBundle
%exclude %{symfony_dir}/Bundle/TwigBundle/*.md
%exclude %{symfony_dir}/Bundle/TwigBundle/composer.json
%exclude %{symfony_dir}/Bundle/TwigBundle/phpunit.*
%exclude %{symfony_dir}/Bundle/TwigBundle/Tests
%exclude %{symfony_dir}/Bundle/TwigBundle/LICENSE

# ------------------------------------------------------------------------------

%files web-profiler-bundle

%doc src/Symfony/Bundle/WebProfilerBundle/*.md
%doc src/Symfony/Bundle/WebProfilerBundle/composer.json
%license src/Symfony/Bundle/WebProfilerBundle/Resources/ICONS_LICENSE.txt
%license src/Symfony/Bundle/WebProfilerBundle/LICENSE

%{symfony_dir}/Bundle/WebProfilerBundle
%exclude %{symfony_dir}/Bundle/WebProfilerBundle/*.md
%exclude %{symfony_dir}/Bundle/WebProfilerBundle/composer.json
%exclude %{symfony_dir}/Bundle/WebProfilerBundle/phpunit.*
%exclude %{symfony_dir}/Bundle/WebProfilerBundle/Tests
%exclude %{symfony_dir}/Bundle/WebProfilerBundle/Resources/ICONS_LICENSE.txt
%exclude %{symfony_dir}/Bundle/WebProfilerBundle/LICENSE

# ------------------------------------------------------------------------------

%files asset

%license src/Symfony/Component/Asset/LICENSE
%doc src/Symfony/Component/Asset/*.md
%doc src/Symfony/Component/Asset/composer.json

%{symfony_dir}/Component/Asset
%exclude %{symfony_dir}/Component/Asset/LICENSE
%exclude %{symfony_dir}/Component/Asset/*.md
%exclude %{symfony_dir}/Component/Asset/composer.json
%exclude %{symfony_dir}/Component/Asset/phpunit.*
%exclude %{symfony_dir}/Component/Asset/Tests

# ------------------------------------------------------------------------------

%files browser-kit

%license src/Symfony/Component/BrowserKit/LICENSE
%doc src/Symfony/Component/BrowserKit/*.md
%doc src/Symfony/Component/BrowserKit/composer.json

%{symfony_dir}/Component/BrowserKit
%exclude %{symfony_dir}/Component/BrowserKit/LICENSE
%exclude %{symfony_dir}/Component/BrowserKit/*.md
%exclude %{symfony_dir}/Component/BrowserKit/composer.json
%exclude %{symfony_dir}/Component/BrowserKit/phpunit.*
%exclude %{symfony_dir}/Component/BrowserKit/Tests

# ------------------------------------------------------------------------------

%files class-loader

%license src/Symfony/Component/ClassLoader/LICENSE
%doc src/Symfony/Component/ClassLoader/*.md
%doc src/Symfony/Component/ClassLoader/composer.json

%{symfony_dir}/Component/ClassLoader
%exclude %{symfony_dir}/Component/ClassLoader/LICENSE
%exclude %{symfony_dir}/Component/ClassLoader/*.md
%exclude %{symfony_dir}/Component/ClassLoader/composer.json
%exclude %{symfony_dir}/Component/ClassLoader/phpunit.*
%exclude %{symfony_dir}/Component/ClassLoader/Tests

# ------------------------------------------------------------------------------

%files config

%license src/Symfony/Component/Config/LICENSE
%doc src/Symfony/Component/Config/*.md
%doc src/Symfony/Component/Config/composer.json

%{symfony_dir}/Component/Config
%exclude %{symfony_dir}/Component/Config/LICENSE
%exclude %{symfony_dir}/Component/Config/*.md
%exclude %{symfony_dir}/Component/Config/composer.json
%exclude %{symfony_dir}/Component/Config/phpunit.*
%exclude %{symfony_dir}/Component/Config/Tests

# ------------------------------------------------------------------------------

%files console

%license src/Symfony/Component/Console/LICENSE
%doc src/Symfony/Component/Console/*.md
%doc src/Symfony/Component/Console/composer.json

%{symfony_dir}/Component/Console
%exclude %{symfony_dir}/Component/Console/LICENSE
%exclude %{symfony_dir}/Component/Console/*.md
%exclude %{symfony_dir}/Component/Console/composer.json
%exclude %{symfony_dir}/Component/Console/phpunit.*
%exclude %{symfony_dir}/Component/Console/Tests

# ------------------------------------------------------------------------------

%files css-selector

%license src/Symfony/Component/CssSelector/LICENSE
%doc src/Symfony/Component/CssSelector/*.md
%doc src/Symfony/Component/CssSelector/composer.json

%{symfony_dir}/Component/CssSelector
%exclude %{symfony_dir}/Component/CssSelector/LICENSE
%exclude %{symfony_dir}/Component/CssSelector/*.md
%exclude %{symfony_dir}/Component/CssSelector/composer.json
%exclude %{symfony_dir}/Component/CssSelector/phpunit.*
%exclude %{symfony_dir}/Component/CssSelector/Tests

# ------------------------------------------------------------------------------

%files debug

%license src/Symfony/Component/Debug/LICENSE
%doc src/Symfony/Component/Debug/*.md
%doc src/Symfony/Component/Debug/composer.json

%{symfony_dir}/Component/Debug
%exclude %{symfony_dir}/Component/Debug/LICENSE
%exclude %{symfony_dir}/Component/Debug/*.md
%exclude %{symfony_dir}/Component/Debug/composer.json
%exclude %{symfony_dir}/Component/Debug/phpunit.*
%exclude %{symfony_dir}/Component/Debug/Tests
%exclude %{symfony_dir}/Component/Debug/Resources/ext

# ------------------------------------------------------------------------------

%files dependency-injection

%license src/Symfony/Component/DependencyInjection/LICENSE
%doc src/Symfony/Component/DependencyInjection/*.md
%doc src/Symfony/Component/DependencyInjection/composer.json

%{symfony_dir}/Component/DependencyInjection
%exclude %{symfony_dir}/Component/DependencyInjection/LICENSE
%exclude %{symfony_dir}/Component/DependencyInjection/*.md
%exclude %{symfony_dir}/Component/DependencyInjection/composer.json
%exclude %{symfony_dir}/Component/DependencyInjection/phpunit.*
%exclude %{symfony_dir}/Component/DependencyInjection/Tests

# ------------------------------------------------------------------------------

%files dom-crawler

%license src/Symfony/Component/DomCrawler/LICENSE
%doc src/Symfony/Component/DomCrawler/*.md
%doc src/Symfony/Component/DomCrawler/composer.json

%{symfony_dir}/Component/DomCrawler
%exclude %{symfony_dir}/Component/DomCrawler/LICENSE
%exclude %{symfony_dir}/Component/DomCrawler/*.md
%exclude %{symfony_dir}/Component/DomCrawler/composer.json
%exclude %{symfony_dir}/Component/DomCrawler/phpunit.*
%exclude %{symfony_dir}/Component/DomCrawler/Tests

# ------------------------------------------------------------------------------

%files event-dispatcher

%license src/Symfony/Component/EventDispatcher/LICENSE
%doc src/Symfony/Component/EventDispatcher/*.md
%doc src/Symfony/Component/EventDispatcher/composer.json

%{symfony_dir}/Component/EventDispatcher
%exclude %{symfony_dir}/Component/EventDispatcher/LICENSE
%exclude %{symfony_dir}/Component/EventDispatcher/*.md
%exclude %{symfony_dir}/Component/EventDispatcher/composer.json
%exclude %{symfony_dir}/Component/EventDispatcher/phpunit.*
%exclude %{symfony_dir}/Component/EventDispatcher/Tests

# ------------------------------------------------------------------------------

%files expression-language

%license src/Symfony/Component/ExpressionLanguage/LICENSE
%doc src/Symfony/Component/ExpressionLanguage/*.md
%doc src/Symfony/Component/ExpressionLanguage/composer.json

%{symfony_dir}/Component/ExpressionLanguage
%exclude %{symfony_dir}/Component/ExpressionLanguage/LICENSE
%exclude %{symfony_dir}/Component/ExpressionLanguage/*.md
%exclude %{symfony_dir}/Component/ExpressionLanguage/composer.json
%exclude %{symfony_dir}/Component/ExpressionLanguage/phpunit.*
%exclude %{symfony_dir}/Component/ExpressionLanguage/Tests

# ------------------------------------------------------------------------------

%files filesystem

%license src/Symfony/Component/Filesystem/LICENSE
%doc src/Symfony/Component/Filesystem/*.md
%doc src/Symfony/Component/Filesystem/composer.json

%{symfony_dir}/Component/Filesystem
%exclude %{symfony_dir}/Component/Filesystem/LICENSE
%exclude %{symfony_dir}/Component/Filesystem/*.md
%exclude %{symfony_dir}/Component/Filesystem/composer.json
%exclude %{symfony_dir}/Component/Filesystem/phpunit.*
%exclude %{symfony_dir}/Component/Filesystem/Tests

# ------------------------------------------------------------------------------

%files finder

%license src/Symfony/Component/Finder/LICENSE
%doc src/Symfony/Component/Finder/*.md
%doc src/Symfony/Component/Finder/composer.json

%{symfony_dir}/Component/Finder
%exclude %{symfony_dir}/Component/Finder/LICENSE
%exclude %{symfony_dir}/Component/Finder/*.md
%exclude %{symfony_dir}/Component/Finder/composer.json
%exclude %{symfony_dir}/Component/Finder/phpunit.*
%exclude %{symfony_dir}/Component/Finder/Tests

# ------------------------------------------------------------------------------

%files form

%license src/Symfony/Component/Form/LICENSE
%doc src/Symfony/Component/Form/*.md
%doc src/Symfony/Component/Form/composer.json

%{symfony_dir}/Component/Form
%exclude %{symfony_dir}/Component/Form/LICENSE
%exclude %{symfony_dir}/Component/Form/*.md
%exclude %{symfony_dir}/Component/Form/composer.json
%exclude %{symfony_dir}/Component/Form/phpunit.*
%exclude %{symfony_dir}/Component/Form/Tests

# ------------------------------------------------------------------------------

%files http-foundation

%license src/Symfony/Component/HttpFoundation/LICENSE
%doc src/Symfony/Component/HttpFoundation/*.md
%doc src/Symfony/Component/HttpFoundation/composer.json

%{symfony_dir}/Component/HttpFoundation
%exclude %{symfony_dir}/Component/HttpFoundation/LICENSE
%exclude %{symfony_dir}/Component/HttpFoundation/*.md
%exclude %{symfony_dir}/Component/HttpFoundation/composer.json
%exclude %{symfony_dir}/Component/HttpFoundation/phpunit.*
%exclude %{symfony_dir}/Component/HttpFoundation/Tests

# ------------------------------------------------------------------------------

%files http-kernel

%license src/Symfony/Component/HttpKernel/LICENSE
%doc src/Symfony/Component/HttpKernel/*.md
%doc src/Symfony/Component/HttpKernel/composer.json

%{symfony_dir}/Component/HttpKernel
%exclude %{symfony_dir}/Component/HttpKernel/LICENSE
%exclude %{symfony_dir}/Component/HttpKernel/*.md
%exclude %{symfony_dir}/Component/HttpKernel/composer.json
%exclude %{symfony_dir}/Component/HttpKernel/phpunit.*
%exclude %{symfony_dir}/Component/HttpKernel/Tests

# ------------------------------------------------------------------------------

%files intl

%license src/Symfony/Component/Intl/LICENSE
%doc src/Symfony/Component/Intl/*.md
%doc src/Symfony/Component/Intl/composer.json

%{symfony_dir}/Component/Intl
%exclude %{symfony_dir}/Component/Intl/LICENSE
%exclude %{symfony_dir}/Component/Intl/*.md
%exclude %{symfony_dir}/Component/Intl/composer.json
%exclude %{symfony_dir}/Component/Intl/phpunit.*
%exclude %{symfony_dir}/Component/Intl/Tests

# ------------------------------------------------------------------------------

%files ldap

%license src/Symfony/Component/Ldap/LICENSE
%doc src/Symfony/Component/Ldap/*.md
%doc src/Symfony/Component/Ldap/composer.json

%{symfony_dir}/Component/Ldap
%exclude %{symfony_dir}/Component/Ldap/LICENSE
%exclude %{symfony_dir}/Component/Ldap/*.md
%exclude %{symfony_dir}/Component/Ldap/composer.json
%exclude %{symfony_dir}/Component/Ldap/phpunit.*
%exclude %{symfony_dir}/Component/Ldap/Tests

# ------------------------------------------------------------------------------

%files locale

%license src/Symfony/Component/Locale/LICENSE
%doc src/Symfony/Component/Locale/*.md
%doc src/Symfony/Component/Locale/composer.json

%{symfony_dir}/Component/Locale
%exclude %{symfony_dir}/Component/Locale/LICENSE
%exclude %{symfony_dir}/Component/Locale/*.md
%exclude %{symfony_dir}/Component/Locale/composer.json
%exclude %{symfony_dir}/Component/Locale/phpunit.*
%exclude %{symfony_dir}/Component/Locale/Tests

# ------------------------------------------------------------------------------

%files options-resolver

%license src/Symfony/Component/OptionsResolver/LICENSE
%doc src/Symfony/Component/OptionsResolver/*.md
%doc src/Symfony/Component/OptionsResolver/composer.json

%{symfony_dir}/Component/OptionsResolver
%exclude %{symfony_dir}/Component/OptionsResolver/LICENSE
%exclude %{symfony_dir}/Component/OptionsResolver/*.md
%exclude %{symfony_dir}/Component/OptionsResolver/composer.json
%exclude %{symfony_dir}/Component/OptionsResolver/phpunit.*
%exclude %{symfony_dir}/Component/OptionsResolver/Tests

# ------------------------------------------------------------------------------

%files process

%license src/Symfony/Component/Process/LICENSE
%doc src/Symfony/Component/Process/*.md
%doc src/Symfony/Component/Process/composer.json

%{symfony_dir}/Component/Process
%exclude %{symfony_dir}/Component/Process/LICENSE
%exclude %{symfony_dir}/Component/Process/*.md
%exclude %{symfony_dir}/Component/Process/composer.json
%exclude %{symfony_dir}/Component/Process/phpunit.*
%exclude %{symfony_dir}/Component/Process/Tests

# ------------------------------------------------------------------------------

%files property-access

%license src/Symfony/Component/PropertyAccess/LICENSE
%doc src/Symfony/Component/PropertyAccess/*.md
%doc src/Symfony/Component/PropertyAccess/composer.json

%{symfony_dir}/Component/PropertyAccess
%exclude %{symfony_dir}/Component/PropertyAccess/LICENSE
%exclude %{symfony_dir}/Component/PropertyAccess/*.md
%exclude %{symfony_dir}/Component/PropertyAccess/composer.json
%exclude %{symfony_dir}/Component/PropertyAccess/phpunit.*
%exclude %{symfony_dir}/Component/PropertyAccess/Tests

# ------------------------------------------------------------------------------

%files property-info

%license src/Symfony/Component/PropertyInfo/LICENSE
%doc src/Symfony/Component/PropertyInfo/*.md
%doc src/Symfony/Component/PropertyInfo/composer.json

%{symfony_dir}/Component/PropertyInfo
%exclude %{symfony_dir}/Component/PropertyInfo/LICENSE
%exclude %{symfony_dir}/Component/PropertyInfo/*.md
%exclude %{symfony_dir}/Component/PropertyInfo/composer.json
%exclude %{symfony_dir}/Component/PropertyInfo/phpunit.*
%exclude %{symfony_dir}/Component/PropertyInfo/Tests

# ------------------------------------------------------------------------------

%files routing

%license src/Symfony/Component/Routing/LICENSE
%doc src/Symfony/Component/Routing/*.md
%doc src/Symfony/Component/Routing/composer.json

%{symfony_dir}/Component/Routing
%exclude %{symfony_dir}/Component/Routing/LICENSE
%exclude %{symfony_dir}/Component/Routing/*.md
%exclude %{symfony_dir}/Component/Routing/composer.json
%exclude %{symfony_dir}/Component/Routing/phpunit.*
%exclude %{symfony_dir}/Component/Routing/Tests

# ------------------------------------------------------------------------------

%files security

%license src/Symfony/Component/Security/LICENSE
%doc src/Symfony/Component/Security/*.md
%doc src/Symfony/Component/Security/composer.json

%{symfony_dir}/Component/Security
%exclude %{symfony_dir}/Component/Security/LICENSE
%exclude %{symfony_dir}/Component/Security/*.md
%exclude %{symfony_dir}/Component/Security/composer.json
%exclude %{symfony_dir}/Component/Security/phpunit.*
%exclude %{symfony_dir}/Component/Security/*/phpunit.*
%exclude %{symfony_dir}/Component/Security/Tests
%exclude %{symfony_dir}/Component/Security/*/Tests
%exclude %{symfony_dir}/Component/Security/*/LICENSE
%exclude %{symfony_dir}/Component/Security/*/*.md
%exclude %{symfony_dir}/Component/Security/*/composer.json

# ------------------------------------------------------------------------------

%files serializer

%license src/Symfony/Component/Serializer/LICENSE
%doc src/Symfony/Component/Serializer/*.md
%doc src/Symfony/Component/Serializer/composer.json

%{symfony_dir}/Component/Serializer
%exclude %{symfony_dir}/Component/Serializer/LICENSE
%exclude %{symfony_dir}/Component/Serializer/*.md
%exclude %{symfony_dir}/Component/Serializer/composer.json
%exclude %{symfony_dir}/Component/Serializer/phpunit.*
%exclude %{symfony_dir}/Component/Serializer/Tests

# ------------------------------------------------------------------------------

%files stopwatch

%license src/Symfony/Component/Stopwatch/LICENSE
%doc src/Symfony/Component/Stopwatch/*.md
%doc src/Symfony/Component/Stopwatch/composer.json

%{symfony_dir}/Component/Stopwatch
%exclude %{symfony_dir}/Component/Stopwatch/LICENSE
%exclude %{symfony_dir}/Component/Stopwatch/*.md
%exclude %{symfony_dir}/Component/Stopwatch/composer.json
%exclude %{symfony_dir}/Component/Stopwatch/phpunit.*
%exclude %{symfony_dir}/Component/Stopwatch/Tests

# ------------------------------------------------------------------------------

%files templating

%license src/Symfony/Component/Templating/LICENSE
%doc src/Symfony/Component/Templating/*.md
%doc src/Symfony/Component/Templating/composer.json

%{symfony_dir}/Component/Templating
%exclude %{symfony_dir}/Component/Templating/LICENSE
%exclude %{symfony_dir}/Component/Templating/*.md
%exclude %{symfony_dir}/Component/Templating/composer.json
%exclude %{symfony_dir}/Component/Templating/phpunit.*
%exclude %{symfony_dir}/Component/Templating/Tests

# ------------------------------------------------------------------------------

%files translation

%license src/Symfony/Component/Translation/LICENSE
%doc src/Symfony/Component/Translation/*.md
%doc src/Symfony/Component/Translation/composer.json

%{symfony_dir}/Component/Translation
%exclude %{symfony_dir}/Component/Translation/LICENSE
%exclude %{symfony_dir}/Component/Translation/*.md
%exclude %{symfony_dir}/Component/Translation/composer.json
%exclude %{symfony_dir}/Component/Translation/phpunit.*
%exclude %{symfony_dir}/Component/Translation/Tests

# ------------------------------------------------------------------------------

%files validator

%license src/Symfony/Component/Validator/LICENSE
%doc src/Symfony/Component/Validator/*.md
%doc src/Symfony/Component/Validator/composer.json

%{symfony_dir}/Component/Validator
%exclude %{symfony_dir}/Component/Validator/LICENSE
%exclude %{symfony_dir}/Component/Validator/*.md
%exclude %{symfony_dir}/Component/Validator/composer.json
%exclude %{symfony_dir}/Component/Validator/phpunit.*
%exclude %{symfony_dir}/Component/Validator/Tests

# ------------------------------------------------------------------------------

%files var-dumper

%license src/Symfony/Component/VarDumper/LICENSE
%doc src/Symfony/Component/VarDumper/*.md
%doc src/Symfony/Component/VarDumper/composer.json

%{symfony_dir}/Component/VarDumper
%exclude %{symfony_dir}/Component/VarDumper/LICENSE
%exclude %{symfony_dir}/Component/VarDumper/*.md
%exclude %{symfony_dir}/Component/VarDumper/composer.json
%exclude %{symfony_dir}/Component/VarDumper/phpunit.*
%exclude %{symfony_dir}/Component/VarDumper/Tests

# ------------------------------------------------------------------------------

%files yaml

%license src/Symfony/Component/Yaml/LICENSE
%doc src/Symfony/Component/Yaml/*.md
%doc src/Symfony/Component/Yaml/composer.json

%{symfony_dir}/Component/Yaml
%exclude %{symfony_dir}/Component/Yaml/LICENSE
%exclude %{symfony_dir}/Component/Yaml/*.md
%exclude %{symfony_dir}/Component/Yaml/composer.json
%exclude %{symfony_dir}/Component/Yaml/phpunit.*
%exclude %{symfony_dir}/Component/Yaml/Tests

# ##############################################################################

%changelog
* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.8.52-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.8.52-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.8.52-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.8.52-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.8.52-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.8.52-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Jul 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.8.52-7
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.8.52-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Oct 26 2020 Remi Collet <remi@remirepo.net> - 2.8.52-5
- raise dependency on PHP 7.0
- drop dependency on symfony/polyfill-php*

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.8.52-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.8.52-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Dec  2 2019 Remi Collet <remi@remirepo.net> - 2.8.52-2
- allow symfony/security-acl v3

* Wed Nov 13 2019 Remi Collet <remi@remirepo.net> - 2.8.52-1
- update to 2.8.52

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.8.51-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Jun 19 2019 Shawn Iwinski <shawn.iwinski@gmail.com> - 2.8.51-2
- Disable tests by default (follows php-symfony3 and php-symfony4 pkgs)
- Always require build dependencies
- Use range version dependencies for Fedora >= 27 || RHEL >= 8
- Bump psr/log min version to 1.0.1 so php-composer(psr/log) virtual provide can be used

* Thu Apr 18 2019 Remi Collet <remi@remirepo.net> - 2.8.51-1
- update to 2.8.51

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.8.49-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Dec  7 2018 Remi Collet <remi@remirepo.net> - 2.8.49-1
- update to 2.8.49

* Tue Nov 27 2018 Remi Collet <remi@remirepo.net> - 2.8.48-1
- update to 2.8.48

* Mon Nov  5 2018 Remi Collet <remi@remirepo.net> - 2.8.47-1
- update to 2.8.47

* Thu Oct 18 2018 Remi Collet <remi@remirepo.net> - 2.8.46-2
- ignore doctrine/data-fixtures version

* Mon Oct  1 2018 Remi Collet <remi@remirepo.net> - 2.8.46-1
- update to 2.8.46

* Tue Aug 28 2018 Remi Collet <remi@remirepo.net> - 2.8.45-1
- update to 2.8.45
- debug and ldap: add missing dependency on common

* Wed Aug 01 2018 Shawn Iwinski <shawn.iwinski@gmail.com> - 2.8.44-1
- Update to 2.8.44 (CVE-2018-14773 / CVE-2018-14774)

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.8.42-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Jun 25 2018 Shawn Iwinski <shawn.iwinski@gmail.com> - 2.8.42-1
- Update to 2.8.42

* Mon May 28 2018 Remi Collet <remi@remirepo.net> - 2.8.41-1
- update to 2.8.41

* Thu May 24 2018 Remi Collet <remi@remirepo.net> - 2.8.40-1
- update to 2.8.40

* Fri May  4 2018 Remi Collet <remi@remirepo.net> - 2.8.39-1
- update to 2.8.39

* Tue Apr 10 2018 Remi Collet <remi@remirepo.net> - 2.8.38-1
- update to 2.8.38

* Tue Apr  3 2018 Remi Collet <remi@remirepo.net> - 2.8.37-1
- update to 2.8.37

* Tue Mar  6 2018 Remi Collet <remi@remirepo.net> - 2.8.36-1
- update to 2.8.36

* Fri Mar  2 2018 Remi Collet <remi@remirepo.net> - 2.8.35-1
- Update to 2.8.35

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.8.34-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Jan 29 2018 Remi Collet <remi@remirepo.net> - 2.8.34-1
- Update to 2.8.34

* Mon Jan  8 2018 Remi Collet <remi@remirepo.net> - 2.8.33-1
- Update to 2.8.33
- don't run Debug test suite which hangs

* Tue Dec  5 2017 Remi Collet <remi@remirepo.net> - 2.8.32-1
- Update to 2.8.32

* Fri Nov 17 2017 Remi Collet <remi@remirepo.net> - 2.8.31-1
- Update to 2.8.31

* Tue Nov 14 2017 Remi Collet <remi@remirepo.net> - 2.8.30-1
- Update to 2.8.30

* Sat Nov 11 2017 Remi Collet <remi@remirepo.net> - 2.8.29-1
- Update to 2.8.29

* Fri Oct  6 2017 Remi Collet <remi@remirepo.net> - 2.8.28-1
- Update to 2.8.28
- ignore unreliable test suite results

* Tue Aug 29 2017 Remi Collet <remi@remirepo.net> - 2.8.27-1
- Update to 2.8.27

* Wed Aug  2 2017 Remi Collet <remi@remirepo.net> - 2.8.26-1
- Update to 2.8.26

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.8.25-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Jul 18 2017 Shawn Iwinski <shawn.iwinski@gmail.com> - 2.8.25-1
- Update to 2.8.25 (CVE-2017-11365)

* Wed Jul  5 2017 Remi Collet <remi@remirepo.net> - 2.8.24-1
- Update to 2.8.24

* Wed Jul  5 2017 Remi Collet <remi@remirepo.net> - 2.8.23-1
- Update to 2.8.23

* Thu Jun  8 2017 Remi Collet <remi@remirepo.net> - 2.8.22-1
- Update to 2.8.22
- raise dependency on twig 1.34 / 2.4 with namespace

* Tue May 30 2017 Remi Collet <remi@remirepo.net> - 2.8.21-1
- Update to 2.8.21
- define RPM_SYMFONY_TREE during the build to ensure dependencies
  use symfony version currently build

* Tue May  2 2017 Remi Collet <remi@remirepo.net> - 2.8.20-1
- Update to 2.8.20

* Wed Apr 12 2017 Shawn Iwinski <shawn.iwinski@gmail.com> - 2.8.19-2
- Add max versions to BuildRequires
- Add max swiftmailer/swiftmailer dependency version
- Prepare for php-phpdocumentor-reflection => php-phpdocumentor-reflection1
  dependency rename

* Wed Apr  5 2017 Remi Collet <remi@remirepo.net> - 2.8.19-1
- Update to 2.8.19

* Mon Mar  6 2017 Remi Collet <remi@remirepo.net> - 2.8.18-1
- Update to 2.8.18

* Mon Feb  6 2017 Remi Collet <remi@fedoraproject.org> - 2.8.17-1
- Update to 2.8.17

* Fri Jan 13 2017 Remi Collet <remi@fedoraproject.org> - 2.8.16-1
- Update to 2.8.16

* Fri Jan  6 2017 Remi Collet <remi@fedoraproject.org> - 2.8.15-4
- fix autoloader for Twig v2
- ignore more tests, FTBFS from Koschei

* Thu Dec 29 2016 Remi Collet <remi@fedoraproject.org> - 2.8.15-1
- Update to 2.8.15

* Tue Nov 22 2016 Remi Collet <remi@fedoraproject.org> - 2.8.14-1
- Update to 2.8.14
- raise dependency on twig 1.28
- force serialize_precision=14 for PHP 7.1 (json tests)

* Thu Oct 27 2016 Remi Collet <remi@fedoraproject.org> - 2.8.13-1
- Update to 2.8.13
- raise dependency on twig 1.27

* Tue Oct 25 2016 Remi Collet <remi@fedoraproject.org> - 2.8.12-3
- fix autoloader

* Tue Oct  4 2016 Remi Collet <remi@fedoraproject.org> - 2.8.12-1
- Update to 2.8.12
- raise dependency on twig 1.26

* Wed Sep 28 2016 Remi Collet <remi@fedoraproject.org> - 2.8.11-2
- add upstream patch to fix FTBFS discovered by Koschei

* Wed Sep  7 2016 Remi Collet <remi@fedoraproject.org> - 2.8.11-1
- Update to 2.8.11

* Mon Sep  5 2016 Remi Collet <remi@fedoraproject.org> - 2.8.10-1
- Update to 2.8.10
- ignore failed tests with ICU 57 or ARM
  https://github.com/symfony/symfony/issues/19854
  https://github.com/symfony/symfony/issues/19856

* Fri Aug  5 2016 Remi Collet <remi@fedoraproject.org> - 2.8.9-2
- fix 1 failed test with latest PHP version, thanks to Koschei
  open https://github.com/symfony/symfony/pull/19539

* Mon Aug  1 2016 Remi Collet <remi@fedoraproject.org> - 2.8.9-1
- Update to 2.8.9

* Fri Jul  1 2016 Remi Collet <remi@fedoraproject.org> - 2.8.8-1
- Update to 2.8.8
- add patch for test suite with phpunit-bridge 2.8
  open https://github.com/symfony/symfony/pull/19255

* Mon Jun  6 2016 Remi Collet <remi@fedoraproject.org> - 2.8.7-1
- Update to 2.8.7

* Sat May 28 2016 Shawn Iwinski <shawn.iwinski@gmail.com> - 2.8.6-2
- Skip test known to fail on RHEL 7

* Tue May 24 2016 Shawn Iwinski <shawn.iwinski@gmail.com> - 2.8.6-1
- Updated to 2.8.6 (RHBZ #1275826)

* Wed May 11 2016 Remi Collet <remi@fedoraproject.org> - 2.7.13-1
- Update to 2.7.13

* Fri Apr 29 2016 Remi Collet <remi@fedoraproject.org> - 2.7.12-2
- Update to 2.7.12
- cleanup autoloader

* Sat Mar 26 2016 Remi Collet <remi@fedoraproject.org> - 2.7.11-2
- Update to 2.7.11
- ignore dependency on symfony/polyfill-mbstring
- ignore Bridge/PhpUnit tests
- ignore tests using DnsMock
  open https://github.com/symfony/symfony/issues/18319
- ignore 1 new online test
- remove PhpUnit/Tests from package

* Fri Mar 25 2016 Remi Collet <remi@fedoraproject.org> - 2.7.10-2
- use php-swiftmailer 5.4.1 instead of old php-swift-Swift

* Mon Feb 29 2016 Remi Collet <remi@fedoraproject.org> - 2.7.10-1
- Update to 2.7.10
- config: add dependency on config (optional)
- routing: add dependency on http-foundation (optional)
- ignore dependency on symfony/polyfill-apcu

* Sun Feb 14 2016 Remi Collet <remi@fedoraproject.org> - 2.7.9-3
- fix test suite with new PHP, upstream patch

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.7.9-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jan 14 2016 Remi Collet <remi@fedoraproject.org> - 2.7.9-2
- fix autoloader for paragonie/random_compat, thanks Koschei

* Thu Jan 14 2016 Remi Collet <remi@fedoraproject.org> - 2.7.9-1
- Update to 2.7.9
- security: add dependency on paragonie/random_compat
- require ircmaxell/password-compat instead of php-password-compat

* Sun Dec 27 2015 Remi Collet <remi@fedoraproject.org> - 2.7.8-1
- Update to 2.7.8

* Wed Nov 25 2015 Remi Collet <remi@fedoraproject.org> - 2.7.7-1
- Update to 2.7.7
- lighter autoloader for components

* Mon Nov  2 2015 Remi Collet <remi@fedoraproject.org> - 2.7.6-2
- add upstream patch for twig 1.23

* Fri Oct 30 2015 Shawn Iwinski <shawn.iwinski@gmail.com> - 2.7.6-1
- Updated to 2.7.6 (RHBZ #1275826)

* Fri Sep 25 2015 Remi Collet <remi@fedoraproject.org> - 2.7.5-1
- Update to 2.7.5
- raise dependency on doctrine/common ~2.4,
  doctrine/dbal ~2.4 and doctrine/orm ^2.4.5
- add optionnal dependency for framework-bundle on serializer

* Wed Sep  9 2015 Remi Collet <remi@fedoraproject.org> - 2.7.4-1
- Update to 2.7.4
- raise dependency on twig/twig ~1.20|~2.0

* Fri Aug  7 2015 Remi Collet <remi@fedoraproject.org> - 2.7.3-3
- rely on PHPUnit 4.8 for test suite

* Fri Jul 31 2015 Remi Collet <remi@fedoraproject.org> - 2.7.3-1
- Update to 2.7.3

* Tue Jul 21 2015 Shawn Iwinski <shawn.iwinski@gmail.com> - 2.7.2-3
- Added patch for symfony/psr-http-message-bridge
- Removed php-mysql dependency from var-dumper

* Mon Jul 13 2015 Shawn Iwinski <shawn.iwinski@gmail.com> - 2.7.2-2
- Updated to 2.7.2 (RHBZ #1242664)

* Sun Jul 05 2015 Shawn Iwinski <shawn.iwinski@gmail.com> - 2.7.1-2
- Remove optional bridge and bundle dependencies in dependency-injection and
  form components.  Add optional text to descriptions.

* Sat Jun 27 2015 Shawn Iwinski <shawn.iwinski@gmail.com> - 2.7.1-1
- Updated to 2.7.1 (RHBZ #1171055)
- Added autoloaders

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.5.12-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed May 27 2015 Remi Collet <remi@fedoraproject.org> - 2.5.12-1
- Update to 2.5.12
- security fix for CVE-2015-4050

* Thu Apr  2 2015 Remi Collet <remi@fedoraproject.org> - 2.5.11-1
- Update to 2.5.11
- security fix for CVE-2015-2308 and CVE-2015-2309

* Wed Mar 18 2015 Remi Collet <remi@fedoraproject.org> - 2.5.10-1
- Update to 2.5.10

* Mon Dec 15 2014 Remi Collet <remi@fedoraproject.org> - 2.5.8-1
- Update to 2.5.8

* Thu Nov 20 2014 Shawn Iwinski <shawn.iwinski@gmail.com> - 2.5.7-1
- Updated to 2.5.7 (BZ #1166396)
- Added php-composer(egulias/email-validator) dependency

* Sun Nov 02 2014 Shawn Iwinski <shawn.iwinski@gmail.com> - 2.5.6-2
- Exclude "intl-data" test group instead of removing test files

* Sun Nov 02 2014 Shawn Iwinski <shawn.iwinski@gmail.com> - 2.5.6-1
- Updated to 2.5.6 (BZ #1157502)
- "php-twig-Twig" dependency updated to "php-composer(twig/twig)"
- Obsoleted php-symfony-icu (data now in intl component)

* Mon Sep 29 2014 Remi Collet <remi@fedoraproject.org> - 2.5.5-1
- update to 2.5.5
- hack PHPUnit autoloader to not use old system symfony
- don't skip any Yaml test

* Wed Sep 03 2014 Shawn Iwinski <shawn.iwinski@gmail.com> - 2.5.4-1
- Updated to 2.5.4 (CVE-2014-6072, CVE-2014-5245, CVE-2014-4931, CVE-2014-6061,
  CVE-2014-5244, BZ #1138285)
- Removed test files from PropertyAccess and Stopwatch components
- Updated skipped tests

* Tue Aug 12 2014 Remi Collet <remi@fedoraproject.org> - 2.5.3-1
- update to 2.5.3
- fix test bootstrap for PHPUnit 4.2

* Sat Jul 19 2014 Remi Collet <remi@fedoraproject.org> - 2.5.2-2
- fix license handling

* Fri Jul 18 2014 Shawn Iwinski <shawn.iwinski@gmail.com> - 2.5.2-1
- Updated to 2.5.2 (BZ #1100720)
- Added php-composer() virtual provides
- Updated most dependencies to use available php-composer virtual provides
- php-password-compat conditional changed from "0%%{?el6}%%{?el7}" to
  ""%%{php_version}" < "5.5""

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.4.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed Apr 30 2014 Shawn Iwinski <shawn.iwinski@gmail.com> - 2.4.4-1
- Updated to 2.4.4 (BZ #1038134)
- Updated Doctrine dependencies
- Sub-pkg phpcompatinfo without Tests directory since they are not pkged

* Mon Feb 17 2014 Shawn Iwinski <shawn.iwinski@gmail.com> - 2.4.2-1
- Updated to 2.4.2 (BZ #1038134)
- Re-enabled tests
- Added expressionlanguage component sub-pkg
- Added provides for security component composer sub-pkgs

* Mon Jan 13 2014 Remi Collet <remi@fedoraproject.org> - 2.3.9-0
- EPEL-7 bootstrap build

* Sun Jan 05 2014 Shawn Iwinski <shawn.iwinski@gmail.com> - 2.3.9-1
- Updated to 2.3.9 (BZ #1038134)
- Conditional %%{?dist}
- Minor bash cosmetic changes
- Skip additional test relying on external resources
- Skip additional el6 test

* Wed Dec 18 2013 Shawn Iwinski <shawn.iwinski@gmail.com> - 2.3.8-1
- Updated to 2.3.8 (BZ #1038134)
- Temporarily skip test known to fail on Fedora > 20

* Sat Dec 14 2013 Remi Collet <remi@fedoraproject.org> - 2.3.7-4
- fix PEAR compatibility: add missing "autoloader.php"

* Tue Nov 26 2013 Shawn Iwinski <shawn.iwinski@gmail.com> - 2.3.7-3
- Fixed several summaries and descriptions ("Symfony2" => "Symfony")

* Fri Nov 22 2013 Shawn Iwinski <shawn.iwinski@gmail.com> - 2.3.7-2
- Renamed from "php-symfony2" to "php-symfony"
- Updated main pkg summary
- Removed dependency on common sub-pkg for sub-pkgs that require other sub-pkgs
- Common sub-pkg obsoletes php-channel-symfony2
- Fixed swiftmailerbridge sub-pkg dependency
- Updated %%check to use PHPUnit's "--include-path" option

* Sun Nov 17 2013 Shawn Iwinski <shawn.iwinski@gmail.com> - 2.3.7-1
- Updated to 2.3.7
- Separated icu pkg
- Added php-password-compat requires for el6 (PHP < 5.5.0)
- common sub-pkg now owns %%{symfony_dir}/{Bridge,Bundle,Component}
- Fixed classloader URL

* Wed Nov 06 2013 Shawn Iwinski <shawn.iwinski@gmail.com> - 2.3.6-2
- Updated tests' autoloader
- Individual pkg tests instead of one
- Skip specific tests
- Exclude tty and benchmark test groups
- Fix main package doc symlink

* Mon Oct 21 2013 Shawn Iwinski <shawn.iwinski@gmail.com> - 2.3.6-1
- Updated to 2.3.6
- Renamed sub-packages to lowercase

* Sat Jul 13 2013 Shawn Iwinski <shawn.iwinski@gmail.com> - 2.3.1-1
- Initial package
