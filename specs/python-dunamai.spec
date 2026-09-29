# Allow disabling integration tests for various version control systems in case
# they are broken with a new Python version or not packaged in a particular
# EPEL branch.
%bcond breezy %{undefined rhel}
%bcond darcs 1
%bcond fossil %[ %{undefined rhel} || %{defined el9} ]
%bcond hg 1
# pijul is not in Fedora yet
%bcond pijul 0
%bcond svn 1

# Is poetry-core too old for the license file to be handled automatically?
%bcond no_pep_639_license %[ %{defined fc43} || %{defined el10} || %{defined el9} ]

%global _description %{expand:
Dunamai is a Python 3.5+ library and command line tool for producing dynamic,
standards-compliant version strings, derived from tags in your version control
system. This facilitates uniquely identifying nightly or per-commit builds in
continuous integration and releasing new versions of your software simply by
creating a tag.}

Name:           python-dunamai
Version:        1.26.2
Release:        %{autorelease}
Summary:        Dynamic version generation

# SPDX
License:        MIT
URL:            https://pypi.org/pypi/dunamai
Source:         https://github.com/mtkennerly/dunamai/archive/v%{version}/%{name}-%{version}.tar.gz

BuildArch:      noarch

%description %_description

%package -n python3-dunamai
Summary:        %{summary}
BuildRequires:  python3-devel

BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(pytest-xdist)

BuildRequires:  /usr/bin/git
%if %{with hg}
BuildRequires:  /usr/bin/hg
%endif
%if %{with darcs}
BuildRequires:  /usr/bin/darcs
%endif
%if %{with svn}
BuildRequires:  /usr/bin/svn
%endif
%if %{with breezy}
BuildRequires:  /usr/bin/bzr
%endif
%if %{with fossil}
BuildRequires:  /usr/bin/fossil
%endif
%if %{with pijul}
BuildRequires:  /usr/bin/pijul
%endif
BuildRequires:  help2man

%description -n python3-dunamai %_description

%prep
%autosetup -p1 -n dunamai-%{version}

# Fix CRLF line endings in documentation
sed -i 's/\r$//' CHANGELOG.md

# see pyproject-rpm-macros documentation for more forms
%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%if %{with no_pep_639_license}
%pyproject_save_files dunamai
%else
%pyproject_save_files --assert-license dunamai
%endif

# generate man pages
for binary in "dunamai" "dunamai check" "dunamai from" "dunamai from any" "dunamai from bazaar" "dunamai from darcs" "dunamai from fossil" "dunamai from git" "dunamai from mercurial" "dunamai from pijul" "dunamai from subversion"
do
    echo "Generating man page for ${binary// /-/}"
    PYTHONPATH="$PYTHONPATH:%{buildroot}/%{python3_sitelib}/" PATH="$PATH:%{buildroot}/%{_bindir}/" help2man --no-info --no-discard-stderr --name="${binary}" --version-string="${binary} %{version}" --output="${binary// /-}.1" "${binary}"
    cat "${binary// /-}.1"
    install -t '%{buildroot}%{_mandir}/man1' -p -m 0644 -D "${binary// /-}.1"
done


%check
%pyproject_check_import

# set up git
git config --global user.email "you@example.com"
git config --global user.name "Your Name"
%if %{with breezy}
# set up bzr
bzr whoami "Your Name <name@example.com>"
%endif
# set up darcs
export DARCS_EMAIL="Yep something <name@example.com>"

# skip test that requires network
%pytest -n auto -v -k "not test__version__from_git__shallow"

%files -n python3-dunamai -f %{pyproject_files}
%doc README.md CHANGELOG.md
%if %{with no_pep_639_license}
%license LICENSE
%endif
%{_bindir}/dunamai
%{_mandir}/man1/dunamai*.1*

%changelog
%autochangelog
