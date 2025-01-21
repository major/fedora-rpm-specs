
Summary:	SRCP based locking table for digital model railroads
Name:		spdrs60
Version:	0.6.5
Release:	7%{?dist}

# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:	GPL-2.0-or-later
URL:		http://spdrs60.sourceforge.net/
Source:		http://sourceforge.net/projects/spdrs60/files/spdrs60/%{version}/spdrs60-%{version}.tar.bz2

BuildRequires:	gcc-c++
BuildRequires:	make
BuildRequires:	desktop-file-utils
BuildRequires:	docbook-style-dsssl
BuildRequires:	qt5-qtbase-devel
BuildRequires:	qt5-qttools-devel
BuildRequires:	openjade

%description
Graphical program to comfortably control a digital model railroad.
Visual appearance and usage comply to the SpDr of the German national
railroad company. SpDrS60 needs a Simple Railroad Command Protocol
(SRCP) server (e.g. erddcd or srcpd) as a link to the physical layout
of the model.

%package	doc
Summary:	Documentation for %{name}
BuildArch:	noarch
Requires:	%{name} = %{version}-%{release}

%description	doc
This package contains documentation for %{name}.

%prep
%setup -q
for file in ./AUTHORS ./NEWS; do
	iconv -f latin1 -t utf8 < $file > $file.new
	mv -f $file.new $file
done

%build
%configure
%make_build

%install
%make_install
%find_lang %{name} --with-man --all-name

cp -p spdrs60.redhat.desktop spdrs60.desktop
desktop-file-install \
	--remove-key='Encoding' \
	--set-key='Terminal' \
	--set-value='false' \
	--remove-category='Application' \
	--delete-original \
	--dir='%{buildroot}%{_datadir}/applications' \
	spdrs60.desktop

%files -f %{name}.lang
%doc AUTHORS README TODO NEWS ChangeLog spdrs60.lsm
%license COPYING
%{_bindir}/%{name}
%{_bindir}/centralclock
%{_datadir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{name}*
%{_mandir}/man1/*.1*

%files doc
%docdir %{_docdir}/%{name}/html
%{_docdir}/%{name}/html

%changelog
* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.5-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 26 2024 Miroslav Suchý <msuchy@redhat.com> - 0.6.5-6
- convert license to SPDX

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.5-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Sep 09 2022 Denis Fateyev <denis@fateyev.com> - 0.6.5-1
- Update to 0.6.5 release

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Oct 21 2021 Denis Fateyev <denis@fateyev.com> - 0.6.4-2
- Spec file cleanup

* Wed Oct 06 2021 Denis Fateyev <denis@fateyev.com> - 0.6.4-1
- Initial Fedora RPM release
