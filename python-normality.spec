%global pypi_name normality

Name:           python-%{pypi_name}
Version:        2.5.0
Release:        %autorelease
Summary:        Tiny library for Python text normalisation

License:        MIT
URL:            https://github.com/pudo/normality
Source:         %url/archive/%{version}/%{pypi_name}-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(pyicu)

%global common_description %{expand:
Normality is a Python micro-package that contains a small set of text
normalization functions for easier re-use. These functions accept a snippet of
unicode or utf-8 encoded text and remove various classes of characters, such as
diacritics, punctuation etc. This is useful as a preparation to further text
analysis.}

%description %{common_description}

%package -n python3-%{pypi_name}
Summary:        %{summary}

%description -n python3-%{pypi_name} %{common_description}

%prep
%autosetup -p1 -n %{pypi_name}-%{version}
sed -i '/\[tool\.setuptools_scm\]/a fallback_version = "%{version}"' pyproject.toml

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files %{pypi_name}

%check
# https://github.com/pudo/normality/issues/20
%pytest -k "not test_guess_encoding and not test_petro_iso_encoded and not test_predict_encoding"

%files -n python3-%{pypi_name} -f %{pyproject_files}
%doc README.md
%license LICENSE

%changelog
%autochangelog
