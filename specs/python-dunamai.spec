# Run breezy/bazaar integration tests?
# Useful to disable when breezy is broken with new Python version.
%bcond breezy 1

%global _description %{expand:
Dunamai is a Python 3.5+ library and command line tool for producing dynamic,
standards-compliant version strings, derived from tags in your version control
system. This facilitates uniquely identifying nightly or per-commit builds in
continuous integration and releasing new versions of your software simply by
creating a tag.}

Name:           python-dunamai
Version:        1.25.0
Release:        %{autorelease}
Summary:        Dynamic version generation

# SPDX
License:        MIT
URL:            https://pypi.org/pypi/dunamai
Source0:        https://github.com/mtkennerly/dunamai/archive/v%{version}/%{name}-%{version}.tar.gz

BuildArch:      noarch

%description %_description

%package -n python3-dunamai
Summary:        %{summary}
BuildRequires:  python3-devel

BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(pytest-xdist)

BuildRequires:  /usr/bin/git
BuildRequires:  /usr/bin/hg
BuildRequires:  /usr/bin/darcs
BuildRequires:  /usr/bin/svn
%if %{with breezy}
BuildRequires:  /usr/bin/bzr
%endif
BuildRequires:  /usr/bin/fossil
BuildRequires:  help2man
# pijul is not in Fedora yet
#BuildRequires:  /usr/bin/pijul

%description -n python3-dunamai %_description

%prep
%autosetup -n dunamai-%{version}

# Comment out to remove /usr/bin/env shebangs
# Can use something similar to correct/remove /usr/bin/python shebangs also
# find . -type f -name "*.py" -exec sed -i '/^#![  ]*\/usr\/bin\/env.*$/ d' {} 2>/dev/null ';'

# see pyproject-rpm-macros documentation for more forms
%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files dunamai

# generate man pages
for binary in "dunamai" "dunamai check" "dunamai from" "dunamai from any" "dunamai from bazaar" "dunamai from darcs" "dunamai from fossil" "dunamai from git" "dunamai from mercurial" "dunamai from pijul" "dunamai from subversion"
do
    echo "Generating man page for ${binary// /-/}"
    PYTHONPATH="$PYTHONPATH:%{buildroot}/%{python3_sitelib}/" PATH="$PATH:%{buildroot}/%{_bindir}/" help2man --no-info --no-discard-stderr --name="${binary}" --version-string="${binary} %{version}" --output="${binary// /-}.1" "${binary}"
    cat "${binary// /-}.1"
    install -t '%{buildroot}%{_mandir}/man1' -p -m 0644 -D "${binary// /-}.1"
done


%check
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
%doc README.md CHANGELOG.md CONTRIBUTING.md
%license LICENSE
%{_bindir}/dunamai
%{_mandir}/man1/dunamai*.1*

%changelog
%autochangelog
