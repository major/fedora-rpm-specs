#
# Fedora spec file for php-aws-sdk3
#
# Copyright (c) 2016-2020 Shawn Iwinski <shawn@iwin.ski>
#
# License: MIT
# http://opensource.org/licenses/MIT
#
# Please preserve changelog entries
#

%global github_owner     aws
%global github_name      aws-sdk-php
%global github_version   3.191.10
%global github_commit    b0e09d3ca2a42edd0b14b9da065376cd3bdd6838

%global composer_vendor  aws
%global composer_project aws-sdk-php

# "php": ">=5.5"
%global php_min_ver 5.5
# "andrewsville/php-token-reflection": "^1.4"
%global tokenreflection_min_ver 1.4
%global tokenreflection_max_ver 2.0
# "aws/aws-php-sns-message-validator": "~1.0"
%global aws_sns_message_validator_min_ver 1.0
%global aws_sns_message_validator_max_ver 2.0
# "doctrine/cache": "~1.4"
#     NOTE: Min version not 1.4 because autoloader required
%global doctrine_cache_min_ver 1.4.1
%global doctrine_cache_max_ver 2.0
# "guzzlehttp/guzzle": "^5.3.3|^6.2.1|^7.0"
%global guzzle_min_ver 5.3.3
%global guzzle_max_ver 8.0
# "guzzlehttp/promises": "^1.4.0"
%global guzzle_promises_min_ver 1.4.0
%global guzzle_promises_max_ver 2.0
# "guzzlehttp/psr7": "^1.7.0"
%global guzzle_psr7_min_ver 1.7.0
%global guzzle_psr7_max_ver 2.0
# "mtdowling/jmespath.php": "^2.6"
%global jmespath_min_ver 2.6
%global jmespath_max_ver 3.0
# "paragonie/random_compat": ">= 2"
#     NOTE: Max version added to prevent issues if v3 is ever released for some reason
%global paragonie_random_compat_min_ver 2.0
%global paragonie_random_compat_max_ver 3.0
# "psr/cache": "^1.0"
%global psr_cache_min_ver 1.0
%global psr_cache_max_ver 2.0
# "psr/simple-cache": "^1.0"
%global psr_simple_cache_min_ver 1.0
%global psr_simple_cache_max_ver 2.0

# tests
%bcond_with tests

# Range dependencies supported?
%if 0%{?fedora} >= 27 || 0%{?rhel} >= 8
%global with_range_dependencies 1
%else
%global with_range_dependencies 0
%endif

%{!?phpdir:  %global phpdir  %{_datadir}/php}

Name:          php-aws-sdk3
Version:       %{github_version}
Release:       %autorelease
Summary:       Amazon Web Services framework for PHP

License:       ASL 2.0
URL:           http://aws.amazon.com/sdkforphp

# GitHub export does not include tests.
# Run php-aws-sdk3-get-source.sh to create full source.
Source0:       %{name}-%{github_version}-%{github_commit}.tar.gz
Source1:       %{name}-get-source.sh

BuildArch:     noarch
# Library version value and autoloader check
BuildRequires: php-cli
## composer.json
BuildRequires: php(language) >= %{php_min_ver}
%if %{with_range_dependencies}
BuildRequires: (php-composer(guzzlehttp/guzzle) >= %{guzzle_min_ver} with php-composer(guzzlehttp/guzzle) < %{guzzle_max_ver})
BuildRequires: (php-composer(guzzlehttp/promises) >= %{guzzle_promises_min_ver} with php-composer(guzzlehttp/promises) < %{guzzle_promises_max_ver})
BuildRequires: (php-composer(guzzlehttp/psr7) >= %{guzzle_psr7_min_ver} with php-composer(guzzlehttp/psr7) < %{guzzle_psr7_max_ver})
BuildRequires: (php-composer(mtdowling/jmespath.php) >= %{jmespath_min_ver} with php-composer(mtdowling/jmespath.php) < %{jmespath_max_ver})
%else
BuildRequires: php-composer(guzzlehttp/guzzle) <  %{guzzle_max_ver}
BuildRequires: php-composer(guzzlehttp/guzzle) >= %{guzzle_min_ver}
BuildRequires: php-composer(guzzlehttp/promises) <  %{guzzle_promises_max_ver}
BuildRequires: php-composer(guzzlehttp/promises) >= %{guzzle_promises_min_ver}
BuildRequires: php-composer(guzzlehttp/psr7) <  %{guzzle_psr7_max_ver}
BuildRequires: php-composer(guzzlehttp/psr7) >= %{guzzle_psr7_min_ver}
BuildRequires: php-composer(mtdowling/jmespath.php) <  %{jmespath_max_ver}
BuildRequires: php-composer(mtdowling/jmespath.php) >= %{jmespath_min_ver}
%endif
## Autoloader
BuildRequires: php-composer(fedora/autoloader)
# Tests
%if %{with tests}
BuildRequires: phpunit8
#BuildRequires: php-composer(phpunit/phpunit)
## Classmap
BuildRequires: php-composer(theseer/autoload)
## composer.json
%if %{with_range_dependencies}
BuildRequires: (php-composer(andrewsville/php-token-reflection) >= %{tokenreflection_min_ver} with php-composer(andrewsville/php-token-reflection) < %{tokenreflection_max_ver})
BuildRequires: (php-composer(aws/aws-php-sns-message-validator) >= %{aws_sns_message_validator_min_ver} with php-composer(aws/aws-php-sns-message-validator) < %{aws_sns_message_validator_max_ver})
BuildRequires: (php-composer(doctrine/cache) >= %{doctrine_cache_min_ver} with php-composer(doctrine/cache) < %{doctrine_cache_max_ver})
BuildRequires: (php-composer(paragonie/random_compat) >= %{paragonie_random_compat_min_ver} with php-composer(paragonie/random_compat) < %{paragonie_random_compat_max_ver})
BuildRequires: (php-composer(psr/cache) >= %{psr_cache_min_ver} with php-composer(psr/cache) < %{psr_cache_max_ver})
BuildRequires: (php-composer(psr/simple-cache) >= %{psr_simple_cache_min_ver} with php-composer(psr/simple-cache) < %{psr_simple_cache_max_ver})
%else
BuildRequires: php-composer(andrewsville/php-token-reflection) <  %{tokenreflection_max_ver}
BuildRequires: php-composer(andrewsville/php-token-reflection) >= %{tokenreflection_min_ver}
BuildRequires: php-composer(aws/aws-php-sns-message-validator) <  %{aws_sns_message_validator_max_ver}
BuildRequires: php-composer(aws/aws-php-sns-message-validator) >= %{aws_sns_message_validator_min_ver}
BuildRequires: php-composer(doctrine/cache) <  %{doctrine_cache_max_ver}
BuildRequires: php-composer(doctrine/cache) >= %{doctrine_cache_min_ver}
BuildRequires: php-composer(paragonie/random_compat) <  %{paragonie_random_compat_max_ver}
BuildRequires: php-composer(paragonie/random_compat) >= %{paragonie_random_compat_min_ver}
BuildRequires: php-composer(psr/cache) <  %{psr_cache_max_ver}
BuildRequires: php-composer(psr/cache) >= %{psr_cache_min_ver}
BuildRequires: php-composer(psr/simple-cache) <  %{psr_simple_cache_max_ver}
BuildRequires: php-composer(psr/simple-cache) >= %{psr_simple_cache_min_ver}
%endif
BuildRequires: php-curl
BuildRequires: php-dom
BuildRequires: php-json
BuildRequires: php-openssl
BuildRequires: php-pcntl
BuildRequires: php-pcre
BuildRequires: php-simplexml
BuildRequires: php-sockets
## phpcompatinfo (computed from version 3.152.0)
BuildRequires: php-date
BuildRequires: php-filter
BuildRequires: php-hash
BuildRequires: php-iconv
BuildRequires: php-libxml
BuildRequires: php-mbstring
BuildRequires: php-posix
BuildRequires: php-reflection
BuildRequires: php-session
BuildRequires: php-soap
BuildRequires: php-spl
BuildRequires: php-tidy
BuildRequires: php-xmlwriter
%endif

# composer.json
Requires:      php(language) >= %{php_min_ver}
%if %{with_range_dependencies}
Requires:      (php-composer(guzzlehttp/guzzle) >= %{guzzle_min_ver} with php-composer(guzzlehttp/guzzle) < %{guzzle_max_ver})
Requires:      (php-composer(guzzlehttp/promises) >= %{guzzle_promises_min_ver} with php-composer(guzzlehttp/promises) < %{guzzle_promises_max_ver})
Requires:      (php-composer(guzzlehttp/psr7) >= %{guzzle_psr7_min_ver} with php-composer(guzzlehttp/psr7) < %{guzzle_psr7_max_ver})
Requires:      (php-composer(mtdowling/jmespath.php) >= %{jmespath_min_ver} with php-composer(mtdowling/jmespath.php) < %{jmespath_max_ver})
%else
Requires:      php-composer(guzzlehttp/guzzle) <  %{guzzle_max_ver}
Requires:      php-composer(guzzlehttp/guzzle) >= %{guzzle_min_ver}
Requires:      php-composer(guzzlehttp/promises) <  %{guzzle_promises_max_ver}
Requires:      php-composer(guzzlehttp/promises) >= %{guzzle_promises_min_ver}
Requires:      php-composer(guzzlehttp/psr7) <  %{guzzle_psr7_max_ver}
Requires:      php-composer(guzzlehttp/psr7) >= %{guzzle_psr7_min_ver}
Requires:      php-composer(mtdowling/jmespath.php) <  %{jmespath_max_ver}
Requires:      php-composer(mtdowling/jmespath.php) >= %{jmespath_min_ver}
%endif
Requires:      php-json
Requires:      php-pcre
Requires:      php-simplexml
# phpcompatinfo (computed from version 3.152.0)
Requires:      php-date
Requires:      php-filter
Requires:      php-hash
Requires:      php-iconv
Requires:      php-libxml
Requires:      php-mbstring
Requires:      php-reflection
Requires:      php-session
Requires:      php-spl
Requires:      php-tidy
Requires:      php-xmlwriter
# Autoloader
Requires:      php-composer(fedora/autoloader)

# Weak dependencies
## composer.json: optional
Suggests:      php-curl
Suggests:      php-openssl
Suggests:      php-sockets
Suggests:      php-composer(doctrine/cache)
Suggests:      php-composer(aws/aws-php-sns-message-validator)

# Composer
Provides:      php-composer(%{composer_vendor}/%{composer_project}) = %{version}

%description
The AWS SDK for PHP makes it easy for developers to access Amazon Web
Services [1] in their PHP code, and build robust applications and software
using services like Amazon S3, Amazon DynamoDB, Amazon Glacier, etc.

Autoloader: %{phpdir}/Aws3/autoload.php

[1] http://aws.amazon.com/


%prep
%setup -qn %{github_name}-%{github_commit}


%build
: Create autoloader
cat <<'AUTOLOAD' | tee src/autoload.php
<?php
/**
 * Autoloader for %{name} and its' dependencies
 * (created by %{name}-%{version}-%{release}).
 */
require_once '%{phpdir}/Fedora/Autoloader/autoload.php';

\Fedora\Autoloader\Autoload::addPsr4('Aws\\', __DIR__);

\Fedora\Autoloader\Dependencies::required([
    __DIR__.'/functions.php',
    [
        '%{phpdir}/GuzzleHttp7/autoload.php',
        '%{phpdir}/GuzzleHttp6/autoload.php',
        '%{phpdir}/GuzzleHttp/autoload.php',
    ],
    '%{phpdir}/GuzzleHttp/Promise/autoload.php',
    '%{phpdir}/GuzzleHttp/Psr7/autoload.php',
    '%{phpdir}/JmesPath/autoload.php',
]);

\Fedora\Autoloader\Dependencies::optional([
    '%{phpdir}/Aws/Sns/autoload.php',
    '%{phpdir}/Doctrine/Common/Cache/autoload.php',
]);
AUTOLOAD


%install
mkdir -p %{buildroot}%{phpdir}/Aws3
cp -pr src/* %{buildroot}%{phpdir}/Aws3/


%check
: Library version value and autoloader check
%{_bindir}/php -r '
    require_once "%{buildroot}%{phpdir}/Aws3/autoload.php";
    $version = \Aws\Sdk::VERSION;
    echo "Version $version (expected %{version})\n";
    exit(version_compare("%{version}", "$version", "=") ? 0 : 1);
'

%if %{with tests}
: Create tests classmap
%{_bindir}/phpab --nolower --output bootstrap.classmap.php build/

: Create tests bootstrap
cat <<'BOOTSTRAP' | tee bootstrap.php
<?php
error_reporting(-1);
date_default_timezone_set('UTC');

require_once '%{buildroot}%{phpdir}/Aws3/autoload.php';

\Fedora\Autoloader\Autoload::addPsr4('Aws\\Test\\', __DIR__.'/tests');
\Fedora\Autoloader\Autoload::addPsr4('TokenReflection\\', '%{phpdir}/TokenReflection');

\Fedora\Autoloader\Dependencies::required([
    __DIR__.'/bootstrap.classmap.php',
    '%{phpdir}/Psr/Cache/autoload.php',
    '%{phpdir}/Psr/SimpleCache/autoload.php',
    '%{phpdir}/random_compat/autoload.php',
]);

class_alias('PHPUnit_Framework_Error_Warning', 'PHPUnit\\Framework\\Error\\Warning');
class_alias('PHPUnit_Framework_Constraint_Callback', 'PHPUnit\\Framework\\Constraint\\Callback');
BOOTSTRAP

: Skip tests known to fail
sed 's/function testValidatesInput/function SKIP_testValidatesInput/' \
    -i tests/Api/ValidatorTest.php
sed -e 's/function testUserAgentAlwaysStartsWithSdkAgentString/function SKIP_testUserAgentAlwaysStartsWithSdkAgentString/' \
    -e 's/function testValidatesCallables/function SKIP_testValidatesCallables/' \
    -e 's/function testValidatesInput/function SKIP_testValidatesInput/' \
    -i tests/ClientResolverTest.php
sed 's/function testEmitsDebugInfo/function SKIP_testEmitsDebugInfo/' \
    -i tests/TraceMiddlewareTest.php
sed -e 's/function testTracksAwsSpecificExceptions/function SKIP_testTracksAwsSpecificExceptions/' \
    -e 's/function testTracksExceptions/function SKIP_testTracksExceptions/' \
    -i tests/TraceMiddlewareTest.php
rm -f \
    tests/Integ/GuzzleV5HandlerTest.php \
    tests/Integ/GuzzleV6StreamHandlerTest.php \
    tests/S3/Crypto/S3EncryptionClientTest.php

: Skip tests that include 64-bit format codes on 32-bit PHP
if [ $(php -r 'echo PHP_INT_SIZE === 4 ? 32 : 64;') == 32 ]
then
    sed -e 's/function testPassesComplianceTest/function SKIP_testPassesComplianceTest/' \
        -e 's/function testEmitsEvents/function SKIP_testEmitsEvents/' \
        -e 's/function testThrowsOnUnknownEventType/function SKIP_testThrowsOnUnknownEventType/' \
        -i tests/Api/Parser/DecodingEventStreamIteratorTest.php
    sed -e 's/function testEmitsEvents/function SKIP_testEmitsEvents/' \
        -e 's/function testThrowsOnUnknownEventType/function SKIP_testThrowsOnUnknownEventType/' \
        -i tests/Api/Parser/EventParsingIteratorTest.php
fi

export AWS_ACCESS_KEY_ID=foo
export AWS_SECRET_ACCESS_KEY=bar

: Upstream tests
%{_bindir}/phpunit8 -d memory_limit=1G --verbose  --testsuite=unit --bootstrap bootstrap.php
%else
: Tests skipped
%endif


%files
%{!?_licensedir:%global license %%doc}
%license LICENSE.md
%doc CHANGELOG.md
%doc composer.json
%doc README.md
%doc UPGRADING.md
%{phpdir}/Aws3


%changelog
%autochangelog
