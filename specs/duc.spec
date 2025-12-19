%if %{undefined el8}
%bcond_without opengl
%else
%ifarch x86_64
%bcond_without opengl
%else
# no glfw-devel
%bcond_with opengl
%endif
%endif

Name:           duc
Version:        1.4.6
Release:        %autorelease
Summary:        Disk usage tools

# src/glad/KHR/khrplatform.h: Khronos
License:        LGPL-3.0-or-later AND MIT-Khronos-old
URL:            https://duc.zevv.nl/
Source0:        https://github.com/zevv/duc/releases/download/%{version}/duc-%{version}.tar.gz
Source1:        duc.desktop

BuildRequires:  cairo-devel
BuildRequires:  desktop-file-utils
BuildRequires:  gcc
%if %{with opengl}
BuildRequires:  glfw-devel
BuildRequires:  libglvnd-devel
%endif
BuildRequires:  ncurses-devel
BuildRequires:  pango-devel
BuildRequires:  pcre2-devel
BuildRequires:  tokyocabinet-devel
BuildRequires:  uthash-devel

%description
Duc is a collection of tools for indexing, inspecting and visualizing
disk usage. Duc maintains a database of accumulated sizes of directories
of the file system, and allows you to query this database with some tools,
or create fancy graphs showing you where your bytes are.


%prep
%autosetup

(
cd src/libduc
for i in ut*.h; do
    ln -sf %{_includedir}/$i $i
done
)


%build
%configure %{?with_opengl:--enable-opengl --disable-x11} \
           %{!?with_opengl:--disable-opengl --enable-x11}
%make_build


%install
%make_install

desktop-file-install --dir=%{buildroot}%{_datadir}/applications %{SOURCE1}


%check
%{buildroot}%{_bindir}/duc help
desktop-file-validate %{buildroot}/%{_datadir}/applications/%{name}.desktop


%files
%license LICENSE
%doc ChangeLog README.md
%{_bindir}/duc
%{_mandir}/man1/duc.1*
%{_datadir}/applications/%{name}.desktop


%changelog
%autochangelog
