%global srcname puzpy

Name:           python-%{srcname}
# The latest GitHub tag is 0.2.4, while the version on pypi is 0.2.5; the
# latter includes an fixup commit and doesn't include tests. For this reason,
# we use the GitHub tarball and add the fixup commit here, but keep the version
# as 0.2.4, as it was never actually bumped in GitHub (see issue #27).
Version:        0.2.4
Release:        %autorelease
Summary:        Python crossword puzzle library

License:        MIT
URL:            https://github.com/alexdej/puzpy
Source:         %{url}/archive/v%{version}/%{srcname}-%{version}.tar.gz
# Missing test file
Source1:        %{url}/raw/2813e095e267b3487e7fecf44981e4f179aeb9ed/testfiles/nyt_v1_4.puz
# Fixup commit
Patch:          %{url}/commit/6109ad5a54359262010d01f2e0175d928bd70962.patch

BuildArch:      noarch
BuildRequires:  python3-devel

%global _description %{expand:
Implementation of .puz crossword puzzle file parser based on the .puz file
format documentation.}

%description %_description

%package -n     python3-%{srcname}
Summary:        %{summary}

%description -n python3-%{srcname} %_description

%prep
%autosetup -p1 -n %{srcname}-%{version}
# Add missing test artifact
cp -p %SOURCE1 testfiles

%generate_buildrequires
%pyproject_buildrequires -t

%build
%pyproject_wheel

%install
%pyproject_install

%check
%tox

%files -n python3-%{srcname}
%doc CHANGELOG.rst README.rst
%pycached %{python3_sitelib}/puz.py
%{python3_sitelib}/%{srcname}-%{version}.dist-info

%changelog
%autochangelog
