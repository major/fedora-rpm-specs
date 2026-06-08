# Main Django, i.e. whether this is the main Django version in the distribution
# that owns /usr/bin/django-admin and other unique paths
# based on Python packaging, see e.g. python3.13
%if 0%{?fedora} >= 42 && 0%{?fedora} < 44
%bcond main_django 1
%else
%bcond main_django 0
%endif

# This allows to build the package without tests, e.g. when bootstrapping new Python version
%bcond tests    1

%if 0%{?python3_version_nodots} >= 315
# some tests currently fail
%bcond all_tests 0
%else
%bcond all_tests 1
%endif

%if %{defined fedora} && 0%{?fedora} == 42
%bcond old_setuptools 1
%else
%bcond old_setuptools 0
%endif

Version:        5.2.15
%global major_ver %(echo %{version} | cut -d. -f1)
Name:           python-django%{major_ver}

Release:        %autorelease
Summary:        A high-level Python Web framework

# Django: BSD-3-Clause
# Bundled Python code: PSF-2.0
# Font Awesome font: OFL-1.1
# Font Awesome icons: MIT
# jquery, select2, xregexp: MIT
# gis/gdal: BSD-3-Clause
# gis/geos: BSD-3-Clause
License:        BSD-3-Clause AND PSF-2.0 AND MIT AND OFL-1.1
URL:            https://www.djangoproject.com/
Source:         %{pypi_source django}
Source:         %{name}.rpmlintrc

# setuptools 77 is only needed to support the new license metadata
Patch1001:      django-allow-setuptools-ge-69.diff

BuildArch:      noarch

%global _description %{expand:
Django is a high-level Python Web framework that encourages rapid
development and a clean, pragmatic design. It focuses on automating as
much as possible and adhering to the DRY (Don't Repeat Yourself)
principle.}

%description %_description


%if %{with main_django}
%global pkgname python3-django
%else
%global pkgname python3-django%{major_ver}
%endif

%package -n %{pkgname}-bash-completion
Summary:        Bash completion files for Django
BuildRequires:  bash-completion
Requires:       bash-completion

# Make sure this replaces any other Django bash-completion package
Provides:       python-django-bash-completion-impl
Conflicts:      python-django-bash-completion-impl

%description -n %{pkgname}-bash-completion
This package contains the Bash completion files form Django high-level
Python Web framework.


%package -n %{pkgname}-doc
Summary:        Documentation for Django
# Font Awesome: CC-BY-4.0, OFL-1.1, MIT
License:        BSD-3-Clause AND CC-BY-4.0 AND OFL-1.1 AND MIT
Suggests:       %{pkgname} = %{version}-%{release}
BuildRequires:  make

# Make sure this replaces any other Django doc package
Provides:       python-django-doc-impl
Conflicts:      python-django-doc-impl

%description -n %{pkgname}-doc
This package contains the documentation for the Django high-level
Python Web framework.


%package -n %{pkgname}
Summary:        A high-level Python Web framework

Recommends:     (%{pkgname}-bash-completion = %{version}-%{release} if bash-completion)

BuildRequires:  python3-devel
BuildRequires:  python3-asgiref

# see django/contrib/admin/static/admin/js/vendor/
Provides:       bundled(jquery) = 3.6.4
Provides:       bundled(select2) = 4.0.13
Provides:       bundled(xregexp) = 3.2.0

# Make sure this replaces any other Django package
Provides:       python-django-impl
Conflicts:      python-django-impl

%description -n %{pkgname} %_description

%prep
%autosetup -N -n django-%{version}
%autopatch -p1 -M 999
%if %{with old_setuptools}
%autopatch -p1 1001
%endif

# hard-code python3 in django-admin
pushd django
for file in conf/project_template/manage.py-tpl ; do
    sed -i "s/\/env python/\/python3/" $file ;
done
popd

# Use non optimised psycopg for tests
# Not available in Fedora
sed -i 's/psycopg\[binary\]>=3\.1\.8/psycopg>=3.1.8/' tests/requirements/postgres.txt

# Remove unnecessary test BRs
sed -i '/^pywatchman\b/d' tests/requirements/py3.txt
sed -i '/^tzdata$/d' tests/requirements/py3.txt

# Remove deps on code checkers/linters
sed -i '/^black\b/d' tests/requirements/py3.txt
sed -i '/^black\b/d' docs/requirements.txt
sed -i '/^blacken-docs\b/d' docs/requirements.txt

%generate_buildrequires
%pyproject_buildrequires -r %{?with_tests:tests/requirements/{py3,postgres,mysql,oracle}.txt} docs/requirements.txt

%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files django

# build documentation
(cd docs && mkdir djangohtml && mkdir -p _build/{doctrees,html} && make html)
mkdir -p %{buildroot}%{_docdir}/python3-django-doc
cp -ar docs/_build/html/* %{buildroot}%{_docdir}/python3-django-doc/

# install man pages (for the main executable only)
mkdir -p %{buildroot}%{_mandir}/man1/
cp -p docs/man/* %{buildroot}%{_mandir}/man1/

# install bash completion script
mkdir -p %{buildroot}%{bash_completions_dir}
install -m 0644 -p extras/django_bash_completion \
  %{buildroot}%{bash_completions_dir}/django-admin

for file in manage.py ; do
   ln -s django-admin.py %{buildroot}%{bash_completions_dir}/$file
done

# remove .po files
find %{buildroot} -name "*.po" | xargs rm -f
sed -i '/.po$/d' %{pyproject_files}

%check
# many contrib modules assume a configured app, "Requested setting INSTALLED_APPS..."
# the rest needs optional dependencies
%{pyproject_check_import \
    -e 'django.contrib.*' \
    -e 'django.core.serializers.pyyaml' \
    -e 'django.db.backends.mysql*' \
    -e 'django.db.backends.oracle*' \
    -e 'django.db.backends.postgresql*'}

%if %{with tests}
cd %{_builddir}/django-%{version}
export PYTHONPATH=$(pwd)
cd tests

%if %{with all_tests}
%{python3} runtests.py --settings=test_sqlite --verbosity=2
%else
%{python3} runtests.py --settings=test_sqlite --verbosity=2 -k "%{shrink:
    not admin_scripts.tests.ArgumentOrder.test_option_then_setting
    and not admin_scripts.tests.ArgumentOrder.test_option_then_setting_then_option
    and not admin_scripts.tests.ArgumentOrder.test_setting_then_option
    and not admin_scripts.tests.ArgumentOrder.test_setting_then_short_option
    and not admin_scripts.tests.ArgumentOrder.test_short_option_then_setting
    and not admin_scripts.tests.CommandDBOptionChoiceTests.test_invalid_choice_db_option
    and not admin_scripts.tests.CommandTypes.test_app_command
    and not admin_scripts.tests.CommandTypes.test_app_command_multiple_apps
    and not admin_scripts.tests.CommandTypes.test_base_command
    and not admin_scripts.tests.CommandTypes.test_base_command_multiple_label
    and not admin_scripts.tests.CommandTypes.test_base_command_no_label
    and not admin_scripts.tests.CommandTypes.test_base_command_with_option
    and not admin_scripts.tests.CommandTypes.test_base_command_with_options
    and not admin_scripts.tests.CommandTypes.test_help_default_options_with_custom_arguments
    and not admin_scripts.tests.CommandTypes.test_label_command
    and not admin_scripts.tests.CommandTypes.test_label_command_multiple_label
    and not admin_scripts.tests.CommandTypes.test_noargs
    and not admin_scripts.tests.CommandTypes.test_specific_help
    and not admin_scripts.tests.CommandTypes.test_suppress_base_options_command_defaults
    and not admin_scripts.tests.CommandTypes.test_suppress_base_options_command_help
    and not admin_scripts.tests.CommandTypes.test_version
    and not admin_scripts.tests.DiffSettings.test_all
    and not admin_scripts.tests.DiffSettings.test_basic
    and not admin_scripts.tests.DiffSettings.test_custom_default
    and not admin_scripts.tests.DiffSettings.test_dynamic_settings_configured
    and not admin_scripts.tests.DiffSettings.test_settings_configured
    and not admin_scripts.tests.DiffSettings.test_unified
    and not admin_scripts.tests.DiffSettings.test_unified_all
    and not admin_scripts.tests.DjangoAdminAlternateSettings.test_builtin_with_environment
    and not admin_scripts.tests.DjangoAdminAlternateSettings.test_builtin_with_settings
    and not admin_scripts.tests.DjangoAdminAlternateSettings.test_custom_command_with_environment
    and not admin_scripts.tests.DjangoAdminAlternateSettings.test_custom_command_with_settings
    and not admin_scripts.tests.DjangoAdminDefaultSettings.test_builtin_with_environment
    and not admin_scripts.tests.DjangoAdminDefaultSettings.test_builtin_with_settings
    and not admin_scripts.tests.DjangoAdminDefaultSettings.test_custom_command_with_environment
    and not admin_scripts.tests.DjangoAdminDefaultSettings.test_custom_command_with_settings
    and not admin_scripts.tests.DjangoAdminFullPathDefaultSettings.test_builtin_with_environment
    and not admin_scripts.tests.DjangoAdminFullPathDefaultSettings.test_builtin_with_settings
    and not admin_scripts.tests.DjangoAdminFullPathDefaultSettings.test_custom_command_with_environment
    and not admin_scripts.tests.DjangoAdminFullPathDefaultSettings.test_custom_command_with_settings
    and not admin_scripts.tests.DjangoAdminMultipleSettings.test_builtin_with_environment
    and not admin_scripts.tests.DjangoAdminMultipleSettings.test_builtin_with_settings
    and not admin_scripts.tests.DjangoAdminMultipleSettings.test_custom_command_with_environment
    and not admin_scripts.tests.DjangoAdminMultipleSettings.test_custom_command_with_settings
    and not admin_scripts.tests.DjangoAdminSettingsDirectory.test_builtin_with_environment
    and not admin_scripts.tests.DjangoAdminSettingsDirectory.test_builtin_with_settings
    and not admin_scripts.tests.DjangoAdminSettingsDirectory.test_setup_environ
    and not admin_scripts.tests.DjangoAdminSettingsDirectory.test_setup_environ_custom_template
    and not admin_scripts.tests.DjangoAdminSettingsDirectory.test_startapp_unicode_name
    and not admin_scripts.tests.ManageAlternateSettings.test_builtin_with_environment
    and not admin_scripts.tests.ManageAlternateSettings.test_builtin_with_settings
    and not admin_scripts.tests.ManageAlternateSettings.test_custom_command_output_color
    and not admin_scripts.tests.ManageAlternateSettings.test_custom_command_with_environment
    and not admin_scripts.tests.ManageAlternateSettings.test_custom_command_with_settings
    and not admin_scripts.tests.ManageCheck.test_app_with_import
    and not admin_scripts.tests.ManageCheck.test_complex_app
    and not admin_scripts.tests.ManageCheck.test_output_format
    and not admin_scripts.tests.ManageCheck.test_warning_does_not_halt
    and not admin_scripts.tests.ManageDefaultSettings.test_builtin_command
    and not admin_scripts.tests.ManageDefaultSettings.test_builtin_with_environment
    and not admin_scripts.tests.ManageDefaultSettings.test_builtin_with_settings
    and not admin_scripts.tests.ManageDefaultSettings.test_custom_command
    and not admin_scripts.tests.ManageDefaultSettings.test_custom_command_with_environment
    and not admin_scripts.tests.ManageDefaultSettings.test_custom_command_with_settings
    and not admin_scripts.tests.ManageFullPathDefaultSettings.test_builtin_command
    and not admin_scripts.tests.ManageFullPathDefaultSettings.test_builtin_with_environment
    and not admin_scripts.tests.ManageFullPathDefaultSettings.test_builtin_with_settings
    and not admin_scripts.tests.ManageFullPathDefaultSettings.test_custom_command
    and not admin_scripts.tests.ManageFullPathDefaultSettings.test_custom_command_with_environment
    and not admin_scripts.tests.ManageFullPathDefaultSettings.test_custom_command_with_settings
    and not admin_scripts.tests.ManageMultipleSettings.test_builtin_with_environment
    and not admin_scripts.tests.ManageMultipleSettings.test_builtin_with_settings
    and not admin_scripts.tests.ManageMultipleSettings.test_custom_command_with_environment
    and not admin_scripts.tests.ManageMultipleSettings.test_custom_command_with_settings
    and not admin_scripts.tests.ManageSettingsWithSettingsErrors.test_help
    and not admin_scripts.tests.StartApp.test_template
    and not admin_scripts.tests.StartApp.test_trailing_slash_in_target_app_directory_name
    and not admin_scripts.tests.StartProject.test_custom_project_template
    and not admin_scripts.tests.StartProject.test_custom_project_template_context_variables
    and not admin_scripts.tests.StartProject.test_custom_project_template_exclude_directory
    and not admin_scripts.tests.StartProject.test_custom_project_template_from_tarball_by_path
    and not admin_scripts.tests.StartProject.test_custom_project_template_from_tarball_by_url
    and not admin_scripts.tests.StartProject.test_custom_project_template_from_tarball_by_url_django_user_agent
    and not admin_scripts.tests.StartProject.test_custom_project_template_from_tarball_to_alternative_location
    and not admin_scripts.tests.StartProject.test_custom_project_template_hidden_directory_default_excluded
    and not admin_scripts.tests.StartProject.test_custom_project_template_hidden_directory_included
    and not admin_scripts.tests.StartProject.test_custom_project_template_non_python_files_not_formatted
    and not admin_scripts.tests.StartProject.test_custom_project_template_with_non_ascii_templates
    and not admin_scripts.tests.StartProject.test_file_without_extension
    and not admin_scripts.tests.StartProject.test_honor_umask
    and not admin_scripts.tests.StartProject.test_no_escaping_of_project_variables
    and not admin_scripts.tests.StartProject.test_project_template_tarball_url
    and not admin_scripts.tests.StartProject.test_simple_project
    and not admin_scripts.tests.StartProject.test_simple_project_different_directory
    and not admin_scripts.tests.StartProject.test_template_dir_with_trailing_slash
    and not logging_tests.tests.SettingsConfigTest.test_circular_dependency
    and not logging_tests.tests.SettingsCustomLoggingTest.test_custom_logging
    and not staticfiles_tests.test_management.TestCollectionHelpSubcommand.test_missing_settings_dont_prevent_help
    and not test_runner.tests.CustomTestRunnerOptionsCmdlineTests.test_no_testrunner
    and not test_runner.tests.CustomTestRunnerOptionsCmdlineTests.test_testrunner_equals
    and not test_runner.tests.CustomTestRunnerOptionsCmdlineTests.test_testrunner_option
    and not test_runner.tests.CustomTestRunnerOptionsSettingsTests.test_all_options_given
    and not test_runner.tests.CustomTestRunnerOptionsSettingsTests.test_default_and_given_options
    and not test_runner.tests.CustomTestRunnerOptionsSettingsTests.test_default_options
    and not test_runner.tests.CustomTestRunnerOptionsSettingsTests.test_option_name_and_value_separated
    and not test_runner.tests.Ticket17477RegressionTests.test_ticket_17477
    and not urlpatterns_reverse.tests.ReverseLazySettingsTest.test_lazy_in_settings
    and not user_commands.tests.CommandRunTests.test_disallowed_abbreviated_options
    and not user_commands.tests.CommandRunTests.test_script_prefix_set_in_commands
    and not user_commands.tests.CommandRunTests.test_skip_checks
    and not user_commands.tests.CommandRunTests.test_subparser_error_formatting
    and not user_commands.tests.CommandRunTests.test_subparser_non_django_error_formatting
}"
%endif
%endif

%files -n %{pkgname}-bash-completion
%{bash_completions_dir}/*

%files -n %{pkgname}-doc
%doc %{_docdir}/python3-django-doc/*
%license LICENSE
%license %{_docdir}/python3-django-doc/_static/fontawesome/LICENSE.txt

%files -n %{pkgname} -f %{pyproject_files}
%doc AUTHORS README.rst
%doc %{python3_sitelib}/django/contrib/admin/static/admin/img/README.txt
%license %{python3_sitelib}/django/contrib/admin/static/admin/css/vendor/select2/LICENSE-SELECT2.md
%license %{python3_sitelib}/django/contrib/admin/static/admin/img/LICENSE
%license %{python3_sitelib}/django/contrib/admin/static/admin/js/vendor/jquery/LICENSE.txt
%license %{python3_sitelib}/django/contrib/admin/static/admin/js/vendor/select2/LICENSE.md
%license %{python3_sitelib}/django/contrib/admin/static/admin/js/vendor/xregexp/LICENSE.txt
%license %{python3_sitelib}/django/contrib/gis/gdal/LICENSE
%license %{python3_sitelib}/django/contrib/gis/geos/LICENSE
%{_bindir}/django-admin
%{_mandir}/man1/django-admin.1*


%changelog
%autochangelog
