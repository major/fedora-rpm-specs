Name:           jrnl
Version:        4.3
Release:        %autorelease
Summary:        Collect your thoughts and notes without leaving the command line

License:        GPL-3.0-only
URL:            https://jrnl.sh
%global forgeurl https://github.com/jrnl-org/jrnl/
Source:         %{forgeurl}/archive/v%{version}/jrnl-%{version}.tar.gz

# Downstream-only: do not upper-bound the Python interpreter version
#
# We must integrate with new Python interpreter versions whether upstream
# is ready or not.
Patch:          0001-Downstream-only-do-not-upper-bound-the-Python-interp.patch
# Downstream-only: do not upper-bound the version of rich
#
# Upstream limits this to the current minor version, but we must integrate
# with new releases whether upstream is ready or not. We would rather deal
# with a few possible, usually-minor test failures than a sudden failure
# to install.
Patch:          0002-Downstream-only-do-not-upper-bound-the-version-of-ri.patch

BuildSystem:            pyproject
BuildOption(install):   -l jrnl
BuildOption(generate_buildrequires): -t

BuildArch:      noarch

BuildRequires:  dos2unix
BuildRequires:  help2man

%description
jrnl is a simple journal application for the command line.

You can use it to easily create, search, and view journal entries. Journals are
stored as human-readable plain text, and can also be encrypted using AES
encryption.


%prep -a
dos2unix --keepdate \
    SECURITY.md \
    docs/external-editors.md \
    docs/journal-types.md \
    docs/reference-command-line.md \
    docs/reference-config-file.md


%install -a
# https://github.com/jrnl-org/jrnl/issues/74
# https://github.com/jrnl-org/jrnl/issues/1274
install -d '%{buildroot}%{_mandir}/man1'
%{py3_test_envvars} help2man --no-info jrnl \
    --output='%{buildroot}%{_mandir}/man1/jrnl.1'


%check -a
# https://github.com/jrnl-org/jrnl/issues/2060#issuecomment-3964203676
k="${k-}${k+ and }not test_install_jrnl_with_custom_expanded_default_journal_path"
k="${k-}${k+ and }not test_install_jrnl_with_custom_relative_default_journal_path"
k="${k-}${k+ and }not test_install_jrnl_with_default_options"
k="${k-}${k+ and }not test_install_jrnl_with_encrypted_default_journal"
k="${k-}${k+ and }not test_install_jrnl_with_encrypted_default_journal_with_no_entries"
k="${k-}${k+ and }not test_update_version_number_in_config_file_when_running_newer_version"

%tox -- -- -k "${k-}" -rs


%files -f %{pyproject_files}
%doc CHANGELOG.md
%doc README.md
%doc docs/

%{_bindir}/jrnl
%{_mandir}/man1/jrnl.1*


%changelog
%autochangelog
