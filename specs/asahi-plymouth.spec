%global _description %{expand:
This is a Plymouth theme for the Asahi Linux distribution for Apple Silicon
Macs.}

Name:           asahi-plymouth
Version:        0.2
Release:        %autorelease
Summary:        Plymouth theme for Asahi Linux

# asahi/asahi.png is CC-BY-SA-4.0, the rest is GPL-3.0-or-later
License:        GPL-3.0-or-later AND CC-BY-SA-4.0
URL:            https://github.com/AsahiLinux/asahi-plymouth
Source:         %{url}/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires:  coreutils

BuildArch:      noarch

%description   %{_description}

%package -n    plymouth-theme-asahi
Summary:       %{summary}
Requires:      plymouth
Provides:      %{name} = %{version}-%{release}

%description -n plymouth-theme-asahi %{_description}

%prep
%autosetup -p1

%build
# Nothing to do

%install
mkdir -p %{buildroot}%{_datadir}/plymouth/themes
cp -pr asahi/ %{buildroot}%{_datadir}/plymouth/themes/

%files -n plymouth-theme-asahi
%license LICENSE
%doc README.md
%{_datadir}/plymouth/themes/asahi/

%changelog
%autochangelog
