Name:           jrnl
Version:        4.2
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

BuildSystem:            pyproject
BuildOption(install):   jrnl
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
# Unpin pytest; see https://github.com/jrnl-org/jrnl/issues/1879.
sed -r -i 's/(pytest\b.*),<=?[[:digit:].]+/\1/' pyproject.toml

dos2unix --keepdate \
    SECURITY.md \
    docs/external-editors.md \
    docs/journal-types.md \
    docs/reference-command-line.md \
    docs/reference-config-file.md


%build -a
# https://github.com/jrnl-org/jrnl/issues/74
# https://github.com/jrnl-org/jrnl/issues/1274
help2man --no-info '%{python3} -m jrnl' --output='jrnl.1'


%install -a
install -D -t '%{buildroot}%{_mandir}/man1' -p -m 0644 'jrnl.1'


%check -a
%tox -- -- -rs


%files -f %{pyproject_files}
%license LICENSE.md

%doc CHANGELOG.md
%doc CODE_OF_CONDUCT.md
%doc CONTRIBUTING.md
%doc README.md
%doc SECURITY.md
%doc docs/

%{_bindir}/jrnl
%{_mandir}/man1/jrnl.1*


%changelog
%autochangelog
