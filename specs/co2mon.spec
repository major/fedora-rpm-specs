%global forgeurl https://github.com/dmage/co2mon
%global commit 6d70750d2140760e23a5d1a4a2cf37f7248d103a
%forgemeta
# override the default forge autosetup directory name because upstream unpacks as dmage-co2mon-<commit_short>
%global forgeautosetupdir dmage-%{name}-%(c=%{commit}; echo ${c:0:7})


Name:           co2mon
Version:        2.1.1
Release:        %autorelease
Summary:        CO2 monitor software

License:        GPL-3.0-or-later
URL:            %{forgeurl}
Source0:        %{forgesource}

BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig(hidapi-libusb)
BuildRequires:  pkgconfig(udev)

Requires:       udev

%description
Software for USB CO2 Monitor devices.

%package        devel
Summary:        Include files for CO2 monitor software
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
Development files for USB CO2 Monitor devices.

%prep
%autosetup -n dmage-%{name}-%(c=%{commit}; echo ${c:0:7})


%build
# TODO: Please submit an issue to upstream (rhbz#2380509)
export CMAKE_POLICY_VERSION_MINIMUM=3.5
%cmake
%cmake_build


%install
%cmake_install

mkdir -p %{buildroot}%{_udevrulesdir}
install -p -m 644 udevrules/99-%{name}.rules %{buildroot}%{_udevrulesdir}

mkdir -p %{buildroot}%{_datadir}/%{name}
cp -r graph %{buildroot}%{_datadir}/%{name}/


%files
%doc README.md
%license LICENSE
%{_bindir}/co2mond
%{_datadir}/%{name}
%{_libdir}/*.so.1*
%{_udevrulesdir}/99-%{name}.rules

%files devel
%{_libdir}/*.so
%{_includedir}/%{name}.h

%changelog
%autochangelog
