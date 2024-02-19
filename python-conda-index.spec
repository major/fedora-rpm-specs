# Circular test dependency on conda-build
%bcond_with bootstrap

Name:           python-conda-index
Version:        0.4.0
Release:        %autorelease
Summary:        Create repodata.json for collections of conda packages
License:        BSD-3-Clause
URL:            https://github.com/conda/conda-index
Source0:        https://github.com/conda/conda-index/archive/%{version}/conda-index-%{version}.tar.gz
BuildRequires:  make
BuildArch:      noarch

%global _description %{expand:
Create repodata.json for collections of conda packages.

The conda_index command operates on a channel directory. A channel directory
contains a noarch subdirectory at a minimum and will almost always contain
other subdirectories named for conda's supported platforms linux-64, win-64,
osx-64, etc. A channel directory cannot have the same name as a supported
platform. Place packages into the same platform subdirectory each archive was
built for. Conda-index extracts metadata from these packages to generate
index.html, repodata.json etc. with summaries of the packages' metadata. Then
conda uses the metadata to solve dependencies before doing an install.

By default, the metadata is output to the same directory tree as the channel
directory, but it can be output to a separate tree with the --output <output>
parameter. The metadata cache is always placed with the packages, in .cache
folders under each platform subdirectory.

After conda-index has finished, its output can be used as a channel conda
install -c file:///path/to/output ... or it would typically be placed on a
web server.
}

%description %_description


%package -n python%{python3_pkgversion}-conda-index
Summary:        %{summary}

BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-myst-parser
BuildRequires:  python%{python3_pkgversion}-sphinx-click

%description -n python%{python3_pkgversion}-conda-index %_description

%prep
%autosetup -p1 -n conda-index-%{version}
# do not run coverage in pytest
sed -i -E '/".*cov.*"/d' pyproject.toml


%generate_buildrequires
%pyproject_buildrequires %{!?with_bootstrap:-x test}


%build
%pyproject_wheel
make man


%install
%pyproject_install
%pyproject_save_files conda_index
mkdir -p %{buildroot}%{_mandir}/man1
install -m644 build/man/conda-index.1 %{buildroot}%{_mandir}/man1/


%if %{without bootstrap}
%check
py.test-%{python3_version} -v
%endif


%files -n python%{python3_pkgversion}-conda-index -f %pyproject_files
# Apparently flit does not mark the licnse automatically
%license %{python3_sitelib}/*.dist-info/LICENSE
%doc CHANGELOG.md README.md
%{_mandir}/man1/conda-index.1*


%changelog
%autochangelog
