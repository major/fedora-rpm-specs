%global _description %{expand:
Dunamai is a Python 3.5+ library and command line tool for producing dynamic,
standards-compliant version strings, derived from tags in your version control
system. This facilitates uniquely identifying nightly or per-commit builds in
continuous integration and releasing new versions of your software simply by
creating a tag.}

Name:           python-dunamai
Version:        1.13.2
Release:        %{autorelease}
Summary:        Dynamic version generation

License:        MIT
URL:            https://pypi.org/pypi/dunamai
Source:         https://github.com/mtkennerly/dunamai/archive/v%{version}/%{name}-%{version}.tar.gz

BuildArch:      noarch

%description %_description

%package -n python3-dunamai
Summary:        %{summary}
BuildRequires:  python3-devel

BuildRequires:  python3-pytest
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

%check
# set up git
git config --global user.email "you@example.com"
git config --global user.name "Your Name"
# set up bzr
brz whoami "Your Name <name@example.com>"
# set up darcs
export DARCS_EMAIL="Yep something <name@example.com>"

%{pytest}

%files -n python3-dunamai -f %{pyproject_files}
%doc README.md CHANGELOG.md CONTRIBUTING.md
%license LICENSE
%{_bindir}/dunamai

%changelog
%autochangelog
