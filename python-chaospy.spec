%bcond_without tests

%global desc %{expand: \
Chaospy is a numerical tool for performing uncertainty quantification using
polynomial.}

Name:           python-chaospy
Version:        4.3.13
Release:        %autorelease
Summary:        Numerical tool for performing uncertainty quantification using polynomial
License:        MIT
URL:            https://github.com/jonathf/chaospy
Source0:        %{url}/archive/v%{version}/chaospy-%{version}.tar.gz
BuildArch:      noarch
# python-chaospy FTBFS on 32-bit architectures
# https://bugzilla.redhat.com/show_bug.cgi?id=2022855
ExcludeArch:    %{ix86} %{arm32}

%description
%{desc}

%package -n python3-chaospy
Summary:        %{summary}

BuildRequires: python3-devel

%if %{with tests}
BuildRequires:  %{py3_dist scikit-learn}
BuildRequires:  %{py3_dist pytest}
BuildRequires:  %{py3_dist importlib-metadata}
%endif

%description -n python3-chaospy
%{desc}

%prep
%autosetup -n chaospy-%{version}

# remove rpm created dir
rm -rf SPECPARTS

# This particular version is required for the tests
# https://github.com/jonathf/chaospy/issues/307#issuecomment-735379840
sed -i 's/numpoly.*/numpoly>=1.2.7/' requirements.txt

%generate_buildrequires
export SETUPTOOLS_SCM_PRETEND_VERSION=%{version}
%pyproject_buildrequires -r

%build
export SETUPTOOLS_SCM_PRETEND_VERSION=%{version}
%pyproject_wheel

%install
export SETUPTOOLS_SCM_PRETEND_VERSION=%{version}
%pyproject_install
%pyproject_save_files chaospy

%check
%if %{with tests}
export PYTHONPATH=$RPM_BUILD_ROOT/%{python3_sitelib}
%{pytest} tests
%endif

%files -n python3-chaospy -f %{pyproject_files}
%doc README.rst

%changelog
%autochangelog
