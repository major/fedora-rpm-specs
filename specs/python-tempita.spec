Name:           python-tempita
Version:        0.6.0
Release:        %autorelease
Summary:        A very small text templating language

License:        MIT
URL:            https://github.com/TurboGears/tempita
Source0:        %{pypi_source tempita}
# https://github.com/TurboGears/tempita/issues/2
# note tag does not quite match version :-(
Source1:        https://raw.githubusercontent.com/TurboGears/tempita/refs/tags/0.6/tests/tests.txt

BuildArch:      noarch

BuildRequires:  python3-devel
# For tests
BuildRequires:  python3-pytest


%global _description %{expand:
Tempita is a small templating language for text substitution.}


%description %_description


%package -n python3-tempita
Summary:        A very small text templating language


%description -n python3-tempita
Tempita is a small templating language for text substitution.


%prep
%autosetup -n tempita-%{version} -p1

cp -p %{SOURCE1} tests/tests.txt


%build
%pyproject_wheel


%generate_buildrequires
%pyproject_buildrequires


%install
%pyproject_install

%pyproject_save_files tempita


%check
%pytest


%files -n python3-tempita -f %{pyproject_files}

%changelog
%autochangelog
