Name:           tikzit
URL:            https://tikzit.github.io/
Version:        2.1.6
Release:        %autorelease
License:        GPLv3+
Summary:        Diagram editor for pgf/TikZ
Source:         https://github.com/%{name}/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz

Requires:       hicolor-icon-theme qt5-qtsvg
BuildRequires: make
BuildRequires:  gcc-c++
BuildRequires:  flex
BuildRequires:  bison
BuildRequires:  qt5-qtbase-devel
BuildRequires:  poppler-qt5-devel
BuildRequires:  desktop-file-utils

%description
TikZiT is a graphical tool for rapidly creating an editing node-and-edge
style graphs. It was originally created to aid in the typesetting of
"dot" diagrams of interacting quantum observables, but can be used as a
general graph editing program.

%prep
%autosetup -n %{name}-%{version}

%build
export OBJCFLAGS="%{optflags}"
%qmake_qt5 PREFIX=%{_prefix}
%make_build V=1
sed -i "s|\r||g" README.md

%install
%make_install INSTALL_ROOT="%{buildroot}"
install -m 644 -D tex/sample/tikzit.sty %{buildroot}%{_datadir}/texlive/texmf-local/tex/latex/tikzit/tikzit.sty
desktop-file-validate %{buildroot}/%{_datadir}/applications/%{name}.desktop

%files
%{_bindir}/tikzit
%license COPYING
%doc README.md
%{_datadir}/mime/packages/user-tikz-document.xml
%{_datadir}/icons/hicolor/*/apps/%{name}.png
%{_datadir}/icons/hicolor/*/apps/%{name}.svg
%{_datadir}/applications/%{name}.desktop
%{_datadir}/texlive/texmf-local/tex/latex/tikzit/tikzit.sty
%{_mandir}/man1/tikzit.1.gz

%changelog
%autochangelog
