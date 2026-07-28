%global pypi_name qudida

Name:           python-%{pypi_name}
Version:        0.0.4
Release:        %autorelease
Summary:        QuDiDA (QUick and DIrty Domain Adaptation)

License:        MIT
URL:            https://github.com/arsenyinfo/qudida
Source0:        %{url}/archive/%{version}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch
Patch0:         001_setup_py.patch
Patch1:         002_fix_sklearn_import.patch

BuildRequires:  python3-devel
BuildRequires:  python3-pkg-resources
BuildRequires:  python3dist(numpy)
BuildRequires:  python3dist(opencv)
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(scikit-learn)
BuildRequires:  python3dist(typing-extensions)

%global _description \
QuDiDA is a micro library for very naive though quick pixel level image domain \
adaptation via scikit-learn transformers. \
Is assumed to be used as image augmentation technique, \
while was not tested in public benchmarks.

%description %{_description}

%package -n     python3-%{pypi_name}
Summary:        %{summary}
%description -n python3-%{pypi_name} %{_description}

%prep
%autosetup -n %{pypi_name}-%{version} -p1

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l %{pypi_name}

%check
%pyproject_check_import
%pytest

%files -n python3-%{pypi_name} -f %{pyproject_files}
%doc README.md


%changelog
%autochangelog
