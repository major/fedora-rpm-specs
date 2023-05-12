Name:           python-pyxdf
Version:        1.16.4
Release:        %autorelease
Summary:        Python package for working with XDF files

License:        BSD-2-Clause
URL:            https://github.com/xdf-modules/pyxdf
Source0:        %{pypi_source pyxdf}
# Required to run some of the tests. This is not mandatory, but why not run all
# the tests we can?  The contents of this archive are licensed (SPDX) MIT, but
# are not installed and do not contribute to the licenses of the binary RPMs.
%global ex_commit 7a66644c6fdbf76a3bff727f8c7c81f2a60213ce
%global ex_url https://github.com/xdf-modules/example-files
Source1:        %{ex_url}/archive/%{ex_commit}/example-files-%{ex_commit}.tar.gz

BuildArch:      noarch
 
BuildRequires:  python3-devel

BuildRequires:  %{py3_dist pytest}

%global common_description %{expand:
pyXDF is a Python importer for XDF files.}

%description %{common_description}


%package -n     python3-pyxdf
Summary:        %{summary}

%description -n python3-pyxdf %{common_description}


%prep
%autosetup -n pyxdf-%{version}
%setup -q -n pyxdf-%{version} -T -D -b 1
ln -s ../example-files-%{ex_commit}/ example-files


%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files pyxdf


%check
%pytest


%files -n python3-pyxdf -f %{pyproject_files}
%doc CHANGELOG.md
%doc README.md


%changelog
%autochangelog
