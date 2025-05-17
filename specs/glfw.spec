Name:           glfw
Version:        3.4
Release:        %autorelease
Epoch:          1
Summary:        A cross-platform multimedia library
Summary(fr):    Une bibliothèque multimédia multi-plateforme
License:        Zlib
URL:            http://www.glfw.org/index.html
Source0:        https://github.com/glfw/glfw/archive/%{version}/%{name}-%{version}.tar.gz
Patch0:         %{name}-doxygen.patch

BuildRequires:  gcc
BuildRequires:  cmake
BuildRequires:  doxygen
BuildRequires:  pkgconfig(dri)
BuildRequires:  pkgconfig(glu)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xcursor)
BuildRequires:  pkgconfig(xi)
BuildRequires:  pkgconfig(xinerama)
BuildRequires:  pkgconfig(xrandr)

BuildRequires:  extra-cmake-modules
BuildRequires:  libxkbcommon-devel
BuildRequires:  vulkan-loader-devel
BuildRequires:  wayland-devel
BuildRequires:  wayland-protocols-devel

%description
GLFW is a free, Open Source, multi-platform library for OpenGL application
development that provides a powerful API for handling operating system specific
tasks such as opening an OpenGL window, reading keyboard, mouse, joystick and
time input, creating threads, and more.

%description -l fr_FR
GLFW est un logiciel gratuit, Open Source, multi-plate-forme de bibliothèque
pour l'application OpenGL développement qui fournit une API puissante pour la
manipulation du système d'exploitation spécifique des tâches telles que
l'ouverture d'une fenêtre OpenGL, la lecture du clavier, souris, joystick et
entrée du temps, les discussions de créer, et plus encore.


%package        devel
Summary:        Development files for %{name}
Summary(fr):    Appui pour le développement d'application C
Requires:       %{name}%{?_isa} = %{epoch}:%{version}-%{release}
Requires:       pkgconfig(dri)
Requires:       pkgconfig(glu)
Requires:       pkgconfig(x11)
Requires:       pkgconfig(xcursor)
Requires:       pkgconfig(xi)
Requires:       pkgconfig(xinerama)
Requires:       pkgconfig(xrandr)

%description devel
The glfw-devel package contains header files for developing glfw
applications.

%description devel -l fr_FR
Le paquet glfw-devel contient les fichiers d'entêtes pour développer
des applications utilisant glfw.


%package        doc
Summary:        Documentation for %{name}
BuildArch:      noarch

%description doc
The %{name}-doc package contains documentation for developing applications
with %{name}.


%prep
%autosetup -p1
find . -type f | xargs sed -i 's/\r//'

%build
%cmake
%cmake_build --target all

%install
%cmake_install

%files
%license LICENSE.md
%doc README.md
%{_libdir}/libglfw.so.3*

%files devel
%{_includedir}/GLFW/
%{_libdir}/libglfw.so
%{_libdir}/pkgconfig/glfw3.pc
%{_libdir}/cmake/glfw3/

%files doc
%doc %{_docdir}/GLFW/

%changelog
%autochangelog
