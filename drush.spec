#
# Fedora spec file for drush
#
# Copyright (c) 2015-2020 Shawn Iwinski <shawn@iwin.ski>
#
# License: MIT
# http://opensource.org/licenses/MIT
#
# Please preserve changelog entries
#

%global github_owner     drush-ops
%global github_name      drush
%global github_version   8.1.16
%global github_commit    bbaff2dc725a5f3eb22006c5de3dc92a2de54b08

%global composer_vendor  drush
%global composer_project drush

# "php": ">=5.4.5"
%global php_min_ver  5.4.5
# "consolidation/annotated-command": "^2.8.1"
%global consolidation_annotated_command_min_ver 2.8.1
%global consolidation_annotated_command_max_ver 5
# "consolidation/output-formatters": "~3"
%global consolidation_output_formatters_min_ver 3
%global consolidation_output_formatters_max_ver 5
# "pear/console_table": "~1.3.1"
%global pear_console_table_min_ver 1.3.1
%global pear_console_table_max_ver 2.0
# "psr/log": "~1.0"
#     NOTE: Min version not 1.0 because autoloader required
%global psr_log_min_ver 1.0.1
%global psr_log_max_ver 2.0
# "psy/psysh": "~0.6"
%global psysh_min_ver 0.6
%global psysh_max_ver 1.0
# "symfony/console": "~2.7",
# "symfony/console": "~2.7|^3",
# "symfony/event-dispatcher": "~2.7",
# "symfony/event-dispatcher": "~2.7|^3",
# "symfony/finder": "~2.7",
# "symfony/finder": "~2.7|^3",
# "symfony/process": "2.7.*"
# "symfony/var-dumper": "~2.7",
# "symfony/yaml": "~2.3",
# "symfony/var-dumper": "~2.7|^3",
# "symfony/yaml": "~2.3|^3",
#     NOTE: Min version not 2.7.0 because autoloader required
%global symfony_min_ver 2.7.1
%global symfony_max_ver 4.0
# "webmozart/path-util": "~2"
%global webmozart_path_util_min_ver 2
%global webmozart_path_util_max_ver 3

%global drush_dir    %{_datadir}/drush
%global pear_channel pear.drush.org
%global pear_name    drush

%global git_min_ver  1.7

# Build using "--with tests" to enable tests
# TODO: Figure out test issues and enable by default
%global with_tests 0%{?_with_tests:1}

%{!?phpdir:  %global phpdir  %{_datadir}/php}

Name:          %{composer_project}
Version:       %{github_version}
Release:       11%{?github_release}%{?dist}
Summary:       Command line shell and scripting interface for Drupal

License:       GPLv2+
URL:           http://www.drush.org/
Source0:       https://github.com/%{github_owner}/%{github_name}/archive/%{github_commit}/%{name}-%{github_version}-%{github_commit}.tar.gz

# error importing function definition for `BASH_FUNC_scl'
# https://github.com/drush-ops/drush/issues/2065
Patch0:        %{name}-issue2065.patch

BuildArch:     noarch
# %%{pear_phpdir} macro
BuildRequires: php-pear
%if %{with_tests}
BuildRequires: git >= %{git_min_ver}
BuildRequires: patch
BuildRequires: php-cli
# composer.json
BuildRequires: php(language) >= %{php_min_ver}
BuildRequires: php-composer(phpunit/phpunit)
%if 0%{?fedora} >= 27 || 0%{?rhel} >= 8
BuildRequires: (php-composer(consolidation/annotated-command) >= %{consolidation_annotated_command_min_ver} with php-composer(consolidation/annotated-command) < %{consolidation_annotated_command_max_ver})
BuildRequires: (php-composer(consolidation/output-formatters) >= %{consolidation_output_formatters_min_ver} with php-composer(consolidation/output-formatters) < %{consolidation_output_formatters_max_ver})
BuildRequires: (php-composer(pear/console_table) >= %{pear_console_table_min_ver} with php-composer(pear/console_table) < %{pear_console_table_max_ver})
BuildRequires: (php-composer(psr/log) >= %{psr_log_min_ver} with php-composer(psr/log) < %{psr_log_max_ver})
BuildRequires: (php-composer(psy/psysh) >= %{psysh_min_ver} with php-composer(psy/psysh) < %{psysh_max_ver})
BuildRequires: (php-composer(symfony/console) >= %{symfony_min_ver} with php-composer(symfony/console) < %{symfony_max_ver})
BuildRequires: (php-composer(symfony/event-dispatcher) >= %{symfony_min_ver} with php-composer(symfony/event-dispatcher) < %{symfony_max_ver})
BuildRequires: (php-composer(symfony/finder) >= %{symfony_min_ver} with php-composer(symfony/finder) < %{symfony_max_ver})
BuildRequires: (php-composer(symfony/process) >= %{symfony_min_ver} with php-composer(symfony/process) < %{symfony_max_ver})
BuildRequires: (php-composer(symfony/var-dumper) >= %{symfony_min_ver} with php-composer(symfony/var-dumper) < %{symfony_max_ver})
BuildRequires: (php-composer(symfony/yaml) >= %{symfony_min_ver} with php-composer(symfony/yaml) < %{symfony_max_ver})
BuildRequires: (php-composer(webmozart/path-util) >= %{webmozart_path_util_min_ver} with php-composer(webmozart/path-util) < %{webmozart_path_util_max_ver})
%else
BuildRequires: php-composer(consolidation/annotated-command) <  %{consolidation_annotated_command_max_ver}
BuildRequires: php-composer(consolidation/annotated-command) >= %{consolidation_annotated_command_min_ver}
BuildRequires: php-composer(consolidation/output-formatters) <  %{consolidation_output_formatters_max_ver}
BuildRequires: php-composer(consolidation/output-formatters) >= %{consolidation_output_formatters_min_ver}
BuildRequires: php-composer(pear/console_table) <  %{pear_console_table_max_ver}
BuildRequires: php-composer(pear/console_table) >= %{pear_console_table_min_ver}
BuildRequires: php-composer(psr/log) <  %{psr_log_max_ver}
BuildRequires: php-composer(psr/log) >= %{psr_log_min_ver}
BuildRequires: php-composer(psy/psysh) <  %{psysh_max_ver}
BuildRequires: php-composer(psy/psysh) >= %{psysh_min_ver}
BuildRequires: php-composer(symfony/console) <  %{symfony_max_ver}
BuildRequires: php-composer(symfony/console) >= %{symfony_min_ver}
BuildRequires: php-composer(symfony/event-dispatcher) <  %{symfony_max_ver}
BuildRequires: php-composer(symfony/event-dispatcher) >= %{symfony_min_ver}
BuildRequires: php-composer(symfony/finder) <  %{symfony_max_ver}
BuildRequires: php-composer(symfony/finder) >= %{symfony_min_ver}
BuildRequires: php-composer(symfony/process) <  %{symfony_max_ver}
BuildRequires: php-composer(symfony/process) >= %{symfony_min_ver}
BuildRequires: php-composer(symfony/var-dumper) <  %{symfony_max_ver}
BuildRequires: php-composer(symfony/var-dumper) >= %{symfony_min_ver}
BuildRequires: php-composer(symfony/yaml) <  %{symfony_max_ver}
BuildRequires: php-composer(symfony/yaml) >= %{symfony_min_ver}
BuildRequires: php-composer(webmozart/path-util) <  %{webmozart_path_util_max_ver}
BuildRequires: php-composer(webmozart/path-util) >= %{webmozart_path_util_min_ver}
%endif
# phpcompatinfo (computed from version 8.1.16)
BuildRequires: php-ctype
BuildRequires: php-date
BuildRequires: php-fileinfo
BuildRequires: php-filter
BuildRequires: php-hash
BuildRequires: php-iconv
BuildRequires: php-json
BuildRequires: php-pcntl
BuildRequires: php-pcre
BuildRequires: php-posix
BuildRequires: php-reflection
BuildRequires: php-simplexml
BuildRequires: php-spl
## Autoloader
BuildRequires: php-composer(fedora/autoloader)
%endif

Requires:      git >= %{git_min_ver}
Requires:      patch
Requires:      php-cli
# composer.json
Requires:      php(language) >= %{php_min_ver}
Requires:      php-composer(phpunit/phpunit)
%if 0%{?fedora} >= 27 || 0%{?rhel} >= 8
Requires:      (php-composer(consolidation/annotated-command) >= %{consolidation_annotated_command_min_ver} with php-composer(consolidation/annotated-command) < %{consolidation_annotated_command_max_ver})
Requires:      (php-composer(consolidation/output-formatters) >= %{consolidation_output_formatters_min_ver} with php-composer(consolidation/output-formatters) < %{consolidation_output_formatters_max_ver})
Requires:      (php-composer(pear/console_table) >= %{pear_console_table_min_ver} with php-composer(pear/console_table) < %{pear_console_table_max_ver})
Requires:      (php-composer(psr/log) >= %{psr_log_min_ver} with php-composer(psr/log) < %{psr_log_max_ver})
Requires:      (php-composer(psy/psysh) >= %{psysh_min_ver} with php-composer(psy/psysh) < %{psysh_max_ver})
Requires:      (php-composer(symfony/console) >= %{symfony_min_ver} with php-composer(symfony/console) < %{symfony_max_ver})
Requires:      (php-composer(symfony/event-dispatcher) >= %{symfony_min_ver} with php-composer(symfony/event-dispatcher) < %{symfony_max_ver})
Requires:      (php-composer(symfony/finder) >= %{symfony_min_ver} with php-composer(symfony/finder) < %{symfony_max_ver})
Requires:      (php-composer(symfony/var-dumper) >= %{symfony_min_ver} with php-composer(symfony/var-dumper) < %{symfony_max_ver})
Requires:      (php-composer(symfony/yaml) >= %{symfony_min_ver} with php-composer(symfony/yaml) < %{symfony_max_ver})
Requires:      (php-composer(webmozart/path-util) >= %{webmozart_path_util_min_ver} with php-composer(webmozart/path-util) < %{webmozart_path_util_max_ver})
%else
Requires:      php-composer(consolidation/annotated-command) <  %{consolidation_annotated_command_max_ver}
Requires:      php-composer(consolidation/annotated-command) >= %{consolidation_annotated_command_min_ver}
Requires:      php-composer(consolidation/output-formatters) <  %{consolidation_output_formatters_max_ver}
Requires:      php-composer(consolidation/output-formatters) >= %{consolidation_output_formatters_min_ver}
Requires:      php-composer(pear/console_table) >= %{pear_console_table_min_ver}
Requires:      php-composer(psr/log) <  %{psr_log_max_ver}
Requires:      php-composer(psr/log) >= %{psr_log_min_ver}
Requires:      php-composer(psy/psysh) <  %{psysh_max_ver}
Requires:      php-composer(psy/psysh) >= %{psysh_min_ver}
Requires:      php-composer(symfony/console) <  %{symfony_max_ver}
Requires:      php-composer(symfony/console) >= %{symfony_min_ver}
Requires:      php-composer(symfony/event-dispatcher) <  %{symfony_max_ver}
Requires:      php-composer(symfony/event-dispatcher) >= %{symfony_min_ver}
Requires:      php-composer(symfony/finder) <  %{symfony_max_ver}
Requires:      php-composer(symfony/finder) >= %{symfony_min_ver}
Requires:      php-composer(symfony/var-dumper) <  %{symfony_max_ver}
Requires:      php-composer(symfony/var-dumper) >= %{symfony_min_ver}
Requires:      php-composer(symfony/yaml) <  %{symfony_max_ver}
Requires:      php-composer(symfony/yaml) >= %{symfony_min_ver}
Requires:      php-composer(webmozart/path-util) <  %{webmozart_path_util_max_ver}
Requires:      php-composer(webmozart/path-util) >= %{webmozart_path_util_min_ver}
%endif
# phpcompatinfo (computed from version 8.1.16)
Requires:      php-ctype
Requires:      php-date
Requires:      php-fileinfo
Requires:      php-filter
Requires:      php-hash
Requires:      php-iconv
Requires:      php-json
Requires:      php-pcre
Requires:      php-posix
Requires:      php-reflection
Requires:      php-simplexml
Requires:      php-spl
# Autoloader
Requires:      php-composer(fedora/autoloader)

# Weak dependencies
%if 0%{?fedora} >= 21
## composer.json: suggest
#Suggests:      php-composer(drush/config-extra)
Suggests:      php-pcntl
## phpcompatinfo
Suggests:      php-pecl(apcu)
Suggests:      php-pecl(Xdebug)
Suggests:      php-pecl(xhprof)
%endif

Provides:      php-composer(%{composer_vendor}/%{composer_project}) = %{version}

Obsoletes:     php-drush-drush < %{version}-%{release}
Provides:      php-drush-drush = %{version}-%{release}
Obsoletes:     drupal6-drush < %{version}-%{release}
Provides:      drupal6-drush = %{version}-%{release}
Obsoletes:     drupal7-drush < %{version}-%{release}
Provides:      drupal7-drush = %{version}-%{release}
Provides:      drupal8-drush = %{version}-%{release}
Provides:      php-pear(%{pear_channel}/%{pear_name}) = %{version}

# This pkg was the only one in this channel so the channel is no longer needed
Obsoletes: php-channel-drush

%description
Drush is a command line shell and Unix scripting interface for Drupal. If you
are unfamiliar with shell scripting, reviewing the documentation for your shell
(e.g. man bash) or reading an online tutorial (e.g. search for "bash tutorial")
will help you get the most out of Drush.

Drush core ships with lots of useful commands for interacting with code like
modules/themes/profiles. Similarly, it runs update.php, executes sql queries
and DB migrations, and misc utilities like run cron or clear cache.


%prep
%setup -qn %{github_name}-%{github_commit}

: Fix "error importing function definition for 'BASH_FUNC_scl'"
: https://github.com/drush-ops/drush/issues/2065
%patch0 -p1

: Remove unneeded stuff
rm -rf drush.bat misc/windrush_build

: W: wrong-file-end-of-line-encoding /usr/share/doc/drush/examples/sandwich.txt
sed -i 's/\r$//' examples/sandwich.txt


%build
: Create autoloader
cat <<'AUTOLOAD' | tee autoload.php
<?php
/**
 * Autoloader for %{name} and its' dependencies
 * (created by %{name}-%{version}-%{release}).
 */
require_once '%{phpdir}/Fedora/Autoloader/autoload.php';

\Fedora\Autoloader\Autoload::addPsr4('Drush\\', __DIR__.'/lib/Drush');

\Fedora\Autoloader\Dependencies::required([
    '%{phpdir}/Consolidation/AnnotatedCommand/autoload.php',
    '%{phpdir}/Consolidation/OutputFormatters/autoload.php',
    '%{phpdir}/Psr/Log/autoload.php',
    '%{phpdir}/Psy/autoload.php',
    [
      '%{phpdir}/Symfony3/Component/Console/autoload.php',
      '%{phpdir}/Symfony/Component/Console/autoload.php',
    ],
    [
      '%{phpdir}/Symfony3/Component/EventDispatcher/autoload.php',
      '%{phpdir}/Symfony/Component/EventDispatcher/autoload.php',
    ],
    [
      '%{phpdir}/Symfony3/Component/Finder/autoload.php',
      '%{phpdir}/Symfony/Component/Finder/autoload.php',
    ],
    [
      '%{phpdir}/Symfony3/Component/VarDumper/autoload.php',
      '%{phpdir}/Symfony/Component/VarDumper/autoload.php',
    ],
    [
      '%{phpdir}/Symfony3/Component/Yaml/autoload.php',
      '%{phpdir}/Symfony/Component/Yaml/autoload.php',
    ],
    '%{phpdir}/Webmozart/PathUtil/autoload.php',
]);

\Fedora\Autoloader\Autoload::addPsr0('Console_', '%{pear_phpdir}');
AUTOLOAD

: Mock Composer autoloader
mkdir vendor
ln -s ../autoload.php vendor/autoload.php


%install
mkdir -p %{buildroot}%{drush_dir}
cp -pr * %{buildroot}%{drush_dir}/

: Bin
mkdir -p %{buildroot}%{_bindir}
ln -s %{drush_dir}/drush %{buildroot}%{_bindir}/drush

: Completion
mkdir -p %{buildroot}%{_sysconfdir}/bash_completion.d
install -pm 0644 drush.complete.sh %{buildroot}%{_sysconfdir}/bash_completion.d/


%check
%if %{with_tests}
: Create tests bootstrap
cat <<'AUTOLOAD' | tee tests-autoload.php
<?php
require_once '%{buildroot}%{drush_dir}/autoload.php';
\Fedora\Autoloader\Autoload::addPsr4('Unish\\', __DIR__.'/tests');
\Fedora\Autoloader\Dependencies::required([
    [
      '%{phpdir}/Symfony3/Component/Process/autoload.php',
      '%{phpdir}/Symfony/Component/Process/autoload.php',
    ],
]);
AUTOLOAD

: Update bootstrap.inc to use generated bootstrap
sed 's#vendor/autoload\.php#tests-autoload.php#' -i tests/bootstrap.inc

: Skip specific tests
pushd tests
    #rm -f \
    #    pmDownloadTest.php \
    #    siteSshTest.php \
    #    sql*Test.php
popd

UNISH_DRUSH=%{buildroot}%{drush_dir}/drush \
    %{_bindir}/phpunit --verbose --configuration tests
%else
: Tests skipped
: Build using "--with tests" to enable tests
%endif


%files
%{!?_licensedir:%global license %%doc}
# %%license
# See https://github.com/drush-ops/drush/pull/319
%doc *.md
%doc composer.json
%doc docs
%doc examples
%doc mkdocs.yml
%{_bindir}/drush
%{drush_dir}
%exclude %{drush_dir}/*.md
%exclude %{drush_dir}/box.json.dist
%exclude %{drush_dir}/composer.json
%exclude %{drush_dir}/docs
%exclude %{drush_dir}/drush.complete.sh
%exclude %{drush_dir}/examples
%exclude %{drush_dir}/mkdocs.yml
%exclude %{drush_dir}/tests
%exclude %{drush_dir}/unish.sh
%{_sysconfdir}/bash_completion.d/drush.complete.sh


%changelog
* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 8.1.16-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 8.1.16-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 8.1.16-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 8.1.16-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 8.1.16-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Feb 24 2020 Shawn Iwinski <shawn@iwin.ski> - 8.1.16-6
- Bump max php-composer(consolidation/annotated-command) and
  php-composer(consolidation/output-formatters) dependency versions

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 8.1.16-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 8.1.16-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 8.1.16-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 8.1.16-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Mar 30 2018 Shawn Iwinski <shawn@iwin.ski> - 8.1.16-1
- Update to 8.1.16
- Add range version dependencies for Fedora >= 27 || RHEL >= 8

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 8.1.10-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 8.1.10-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Mar 28 2017 Shawn Iwinski <shawn@iwin.ski> - 8.1.10-2
- Add max versions to BuildRequires
- Prepare for php-phpdocumentor-reflection-docblock =>
  php-phpdocumentor-reflection-docblock2 dependency rename

* Tue Feb 28 2017 Shawn Iwinski <shawn@iwin.ski> - 8.1.10-1
- Update to 8.1.10 (RHBZ #1426457)

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 8.1.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sun Jan 15 2017 Shawn Iwinski <shawn@iwin.ski> - 8.1.9-1
- Update to 8.1.9 (RHBZ #1413321)

* Tue Dec 20 2016 Shawn Iwinski <shawn@iwin.ski> - 8.1.8-3
- Add missing php-composer(fedora/autoloader) dependency (RHBZ #1406416)

* Sat Dec 03 2016 Shawn Iwinski <shawn@iwin.ski> - 8.1.8-2
- Fix autoloader

* Sat Dec 03 2016 Shawn Iwinski <shawn@iwin.ski> - 8.1.8-1
- Update to 8.1.8 (RHBZ #1400079)
- Switch autoloader from php-composer(symfony/class-loader) to
  php-composer(fedora/autoloader)

* Wed Nov 02 2016 Shawn Iwinski <shawn@iwin.ski> - 8.1.7-2
- Remove %%{_sysconfdir}/bash_completion.d directory ownership (RHBZ #1375595)
- Add php-cli build dependency

* Tue Nov 01 2016 Shawn Iwinski <shawn@iwin.ski> - 8.1.7-1
- Update to 8.1.7 (RHBZ #1388273)

* Fri Aug 19 2016 Shawn Iwinski <shawn@iwin.ski> - 8.1.3-3
- Add patch to fix "error importing function definition for `BASH_FUNC_scl'"

* Wed Aug 10 2016 Shawn Iwinski <shawn@iwin.ski> - 8.1.3-2
- Increase "consolidation/annotated-command" max version

* Tue Aug 09 2016 Shawn Iwinski <shawn@iwin.ski> - 8.1.3-1
- Update to 8.1.3 (RHBZ #1357097)

* Mon Jun 27 2016 Shawn Iwinski <shawn@iwin.ski> - 6.7.0-3
- EPEL6 requires "php-pear-Console-Table" instead of "php-composer(pear/console_table)"

* Sat Jun 18 2016 Shawn Iwinski <shawn@iwin.ski> - 6.7.0-2
- Add missing "php-composer(pear/console_table)" dependency (RHBZ #1347826)

* Fri May 06 2016 Shawn Iwinski <shawn@iwin.ski> - 6.7.0-1
- Update to 6.7.0

* Sun Jul 19 2015 Shawn Iwinski <shawn@iwin.ski> - 6.6.0-1
- Initial package obsoleting php-drush-drush
