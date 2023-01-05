# no tests in pypi tar and they haven't tagged any releases on GitHub so we
# can't use tars from there.

%global _description %{expand:
Lazy transposing and slicing of h5py Datasets and zarr arrays}

Name:           python-lazy-ops
Version:        0.2.0
Release:        %{autorelease}
Summary:        Lazy transposing and slicing of h5py and Zarr Datasets

License:        BSD
URL:            https://pypi.org/pypi/lazy_ops
Source0:        %{pypi_source lazy_ops}
# Not included in PyPi, issue filed
# https://github.com/catalystneuro/lazy_ops/issues/26
Source1:        https://github.com/catalystneuro/lazy_ops/raw/407504d1c4b1447e9527e7bddd771b6cc6f4810a/LICENSE

BuildArch:      noarch

# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch: %{ix86}

%description %_description

%package -n python3-lazy-ops
Summary:        %{summary}
BuildRequires:  python3-devel
# Not listed in requirements
# PR for future releases:
# https://github.com/catalystneuro/lazy_ops/pull/27
BuildRequires:  %{py3_dist numpy}

%description -n python3-lazy-ops %_description

%prep
%autosetup -n lazy_ops-%{version}

cp %{SOURCE1} .

%generate_buildrequires
%pyproject_buildrequires -r

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files lazy_ops

%check
%py3_check_import lazy_ops

%files -n python3-lazy-ops -f %{pyproject_files}
%doc README.md

%changelog
%autochangelog
