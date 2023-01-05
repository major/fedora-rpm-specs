%global _description %{expand:
Dunamai is a Python 3.5+ library and command line tool for producing dynamic,
standards-compliant version strings, derived from tags in your version control
system. This facilitates uniquely identifying nightly or per-commit builds in
continuous integration and releasing new versions of your software simply by
creating a tag.}

Name:           python-dunamai
Version:        1.15.0
Release:        %{autorelease}
Summary:        Dynamic version generation

# SPDX
License:        MIT
URL:            https://pypi.org/pypi/dunamai
Source0:        https://github.com/mtkennerly/dunamai/archive/v%{version}/%{name}-%{version}.tar.gz

# Man pages hand-written for Fedora in groff_man(7) format based on --help
Source100:      dunamai.1
Source200:      dunamai-check.1
Source300:      dunamai-from.1
Source301:      dunamai-from-any.1
Source302:      dunamai-from-bazaar.1
Source303:      dunamai-from-darcs.1
Source304:      dunamai-from-fossil.1
Source305:      dunamai-from-git.1
Source306:      dunamai-from-mercurial.1
Source307:      dunamai-from-pijul.1
Source308:      dunamai-from-subversion.1

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
BuildRequires:  /usr/bin/bzr
BuildRequires:  /usr/bin/fossil
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
install -t '%{buildroot}%{_mandir}/man1' -p -m 0644 -D \
    '%{SOURCE100}' '%{SOURCE200}' '%{SOURCE300}' '%{SOURCE301}' \
    '%{SOURCE302}' '%{SOURCE303}' '%{SOURCE304}' '%{SOURCE305}' \
    '%{SOURCE306}' '%{SOURCE307}' '%{SOURCE308}'

%check
# set up git
git config --global user.email "you@example.com"
git config --global user.name "Your Name"
# set up bzr
brz whoami "Your Name <name@example.com>"
# set up darcs
export DARCS_EMAIL="Yep something <name@example.com>"

%pytest -n auto -v

%files -n python3-dunamai -f %{pyproject_files}
%doc README.md CHANGELOG.md CONTRIBUTING.md
%license LICENSE
%{_bindir}/dunamai
%{_mandir}/man1/dunamai*.1*

%changelog
%autochangelog
