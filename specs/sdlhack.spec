Name:           sdlhack
Version:        1.4
Release:        %autorelease
Summary:        Force full-screen games to minimize

# Upstream files specify LGPL v2.1 or later
License:        LGPL-2.1-or-later
URL:            http://jspenguin.org:81/software/sdlhack/
Source0:        http://jspenguin.org:81/software/%{name}/%{name}-%{version}.tar.gz
Source1:        %{name}.1
BuildRequires:  gcc
BuildRequires:  SDL-devel

%description
SDLHack is a wrapper for SDL which lets you force full-screen games to minimize.
It also allows you to disable joystick detection. 

%prep
%autosetup
# Change the path of the library since we install it in a private libdir
sed -i 's|lib%{name}.so|%{_libdir}/%{name}/lib%{name}.so|g' sdlhack

# Remove any prebuilt libs
rm -f *.so

%build
gcc %{optflags} %{build_ldflags} $(sdl-config --cflags) -shared -fPIC -ldl -Wall lib%{name}.c -o lib%{name}.so

%install
mkdir -p %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_libdir}/%{name}
mkdir -p %{buildroot}%{_mandir}/man1
install -Dpm 755 %{name} %{buildroot}%{_bindir}
# Install libsdlhack.so in a private libdir since it is only used by this program
install -Dpm 755 lib%{name}.so %{buildroot}%{_libdir}/%{name}
install -Dpm 644 %{SOURCE1} %{buildroot}%{_mandir}/man1


%files
%doc README
%license COPYING
%{_bindir}/%{name}
%dir %{_libdir}/%{name}
%{_libdir}/%{name}/lib%{name}.so
%{_mandir}/man1/%{name}.1.gz

%changelog
%autochangelog
