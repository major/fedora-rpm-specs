%global srcname fedfind

Name:           fedfind
Version:        6.1.4
Release:        %autorelease
Summary:        Fedora compose and image finder

License:        GPL-3.0-or-later
URL:            https://forge.fedoraproject.org/quality/fedfind
Source0:        https://files.pythonhosted.org/packages/source/f/%{srcname}/%{srcname}-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  python3-devel
Requires:       python%{python3_pkgversion}-fedfind

%description
Fedora Finder finds Fedora. For now, that means it finds Fedora images
- for stable releases, milestone pre-releases, candidate composes, and
nightly composes. The fedfind package provides a simple CLI for showing
image URLs.

%package -n python%{python3_pkgversion}-fedfind
Summary:        Fedora Finder finds Fedora (using Python 3)
%{?python_provide:%python_provide python%{python3_pkgversion}-fedfind}

%description -n python%{python3_pkgversion}-fedfind
Fedora Finder finds Fedora. For now, that means it finds Fedora images
- for stable releases, milestone pre-releases, candidate composes, and
nightly composes. The fedfind library provides a handy interface for
interacting with Fedora composes and discovering various properties of
them, along with some miscellaneous helper functions. This is the
Python 3 library package.


%prep
%autosetup -n %{srcname}-%{version} -p1
# setuptools-scm is needed to build the source distribution, but not
# for packaging, which *starts* from the source distribution
sed -i -e 's., "setuptools-scm"..g' pyproject.toml

%generate_buildrequires
%pyproject_buildrequires -t

%build
%pyproject_wheel

%install
%pyproject_install

%check
%tox

%files
%doc README.md CHANGELOG.md
%license COPYING
%{_bindir}/fedfind

%files -n python%{python3_pkgversion}-fedfind
%doc README.md CHANGELOG.md
%license COPYING
%{python3_sitelib}/%{srcname}*

%changelog
%autochangelog
