Name:           jrnl
Version:        3.0
Release:        %autorelease
Summary:        Collect your thoughts and notes without leaving the command line

License:        GPL-3.0-only
URL:            https://jrnl.sh
%global forgeurl https://github.com/jrnl-org/jrnl/
Source0:        %{forgeurl}/archive/v%{version}/jrnl-%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  python3-devel

BuildRequires:  help2man

%description
jrnl is a simple journal application for the command line.

You can use it to easily create, search, and view journal entries. Journals are
stored as human-readable plain text, and can also be encrypted using AES
encryption.


%package doc
Summary:        Documentation for jrnl

# The mkdocs-generated HTML documentation is not suitable for packaging; see
# https://bugzilla.redhat.com/show_bug.cgi?id=2006555 for discussion.
#
# We can package the Markdown sources without building them; they are still
# relatively legible as plain text.

%description doc
The jrnl-doc package contains detailed documentation for jrnl.


%prep
%autosetup -n jrnl-%{version} -p1

# Exception: gherkin-terminal-reporter is not compatible with 'xdist' plugin.
# https://github.com/pytest-dev/pytest-bdd/issues/501
sed -r -i '/"--gherkin-terminal-reporter"/d' pyproject.toml


%generate_buildrequires
%pyproject_buildrequires -t


%build
%pyproject_wheel

# https://github.com/jrnl-org/jrnl/issues/74
# https://github.com/jrnl-org/jrnl/issues/1274
help2man --no-info '%{python3} -m jrnl' --output='jrnl.1'


%install
%pyproject_install
%pyproject_save_files jrnl

install -D -t '%{buildroot}%{_mandir}/man1' -p -m 0644 'jrnl.1'


%check
%tox


%files -f %{pyproject_files}
%license LICENSE.md
%{_bindir}/jrnl
%{_mandir}/man1/jrnl.1*


%files doc
%license LICENSE.md
%doc CHANGELOG.md
%doc CODE_OF_CONDUCT.md
%doc CONTRIBUTING.md
%doc README.md
%doc SECURITY.md
%doc docs/


%changelog
%autochangelog
