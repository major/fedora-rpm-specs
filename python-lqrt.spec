%global forgeurl https://github.com/alyakin314/lqrt
# No tag on GitHub, and no sources on Pypi
# https://github.com/alyakin314/lqrt/issues/1
%global commit e2c250d46669bea7d294c514b407631027ae015e
# Do not use dist prefix since it's not a snapshot
%global distprefix %{nil}


Name:       python-lqrt
Version:    0.3.3
Release:    %autorelease
Summary:    Hypothesis Testing of Location Parameters using Lq-Likelihood-Ratio-Type Test
%forgemeta

License:    GPL-3.0-only
URL:        %forgeurl
Source0:    %forgesource

BuildArch:  noarch


%global _description %{expand:
This package implements a robust hypothesis testing procedure: the
Lq-likelihood-ratio-type test (LqRT), introduced in Qin and Priebe (2017). The
code replicates and extends the R package which can be found here:
http://homepages.uc.edu/~qinyn/LqLR/

The paper supporting this package is currently in review; a preprint can be
found here:
https://arxiv.org/abs/1911.11922
}

%description %_description

%package -n python3-lqrt
Summary:    Hypothesis Testing of Location Parameters using Lq-Likelihood-Ratio-Type Test
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools)

%description -n python3-lqrt %_description

%prep
%forgesetup

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files lqrt

%check
%pyproject_check_import

%files -n python3-lqrt -f %{pyproject_files}
%doc README.md

%changelog
%autochangelog
