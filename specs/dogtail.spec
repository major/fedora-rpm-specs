Summary:        GUI test tool and automation framework
Name:           dogtail
Version:        2.0.4
Release:        %autorelease
License:        GPL-2.0-only
URL:            https://gitlab.com/dogtail/dogtail
Source0:        %{pypi_source dogtail}
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3-pip
BuildRequires:  python3-setuptools >= 80
BuildRequires:  python3-setuptools-scm >= 8
BuildRequires:  python3-wheel

%global _description %{expand:
GUI test tool and automation framework that uses Accessibility (AT-SPI)
technologies to communicate with desktop applications.}

%description %{_description}

%package -n python3-dogtail
Summary:        %{summary}
Requires:       python3-gobject
Requires:       python3-packaging
Requires:       gnome-ponytail-daemon
# Scripts subpackage merged into main package in 2.0.4
Obsoletes:      python3-dogtail-scripts < 2.0.0

%description -n python3-dogtail
%{_description}

%prep
%autosetup -p1

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files dogtail
# Remove tests installed by upstream's pyproject.toml packaging
rm -rf %{buildroot}%{python3_sitelib}/tests/

%files -n python3-dogtail -f %{pyproject_files}
%license COPYING
%doc README.md NEWS
%{_bindir}/dogtail-create-config
%{_bindir}/dogtail-get-config
%{_bindir}/dogtail-headless

%changelog
%autochangelog
