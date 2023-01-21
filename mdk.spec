Name:		mdk
Version:	1.2.10
Release:	6%{?dist}
Summary:	GNU MIX Development Kit

License:	GPLv3+ and GFDL
URL:		http://www.gnu.org/software/mdk/
Source0:	http://ftp.gnu.org/gnu/mdk/v%{version}/%{name}-%{version}.tar.gz
Source1:	mdk.desktop
Patch0:		glib-deprecated.patch

BuildRequires: make
BuildRequires:  gcc
BuildRequires:	guile22-devel
BuildRequires:	libglade2-devel
BuildRequires:	gettext
BuildRequires:	desktop-file-utils
BuildRequires:	readline-devel
BuildRequires:	ncurses-devel
BuildRequires:	intltool

%package	doc
Summary:	GNU MIX Development Kit Documentation and Samples
BuildArch:	noarch

%description
MDK stands for MIX Development Kit, and provides tools for developing
and executing, in a MIX virtual machine, MIXAL programs.

The MIX is Donald Knuth's mythical computer, described in the first
volume of The Art of Computer Programming, which is programmed using
MIXAL, the MIX assembly language.

MDK includes a MIXAL assembler (mixasm) and a MIX virtual machine
(mixvm) with a command line interface.  In addition, a GTK+ GUI to
mixvm, called gmixvm, is provided; and, in case you are an Emacs guy,
you can try misc/mixvm.el, which allows running mixvm inside an Emacs
GUD buffer.

Using these interfaces, you can debug your MIXAL programs at source
code level, and read/modify the contents of all the components of the
MIX computer (including block devices, which are simulated using the
file system).

%description doc
Samples and documentation for the MDK package.

%prep
%autosetup -p1

%build
autoconf
%configure
%{make_build}

%install
%{make_install}
rm -f $RPM_BUILD_ROOT/%{_infodir}/dir
desktop-file-install \
	--dir=${RPM_BUILD_ROOT}%{_datadir}/applications \
	%{SOURCE1}

%find_lang %{name}

%files -f %{name}.lang
%license COPYING
%doc AUTHORS README THANKS
%{_bindir}/mixasm
%{_bindir}/mixvm
%{_bindir}/gmixvm
%{_bindir}/mixguile
%{_datadir}/mdk
%{_infodir}/*
%{_datadir}/applications/mdk.desktop

%files doc
%doc samples doc

%changelog
* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.10-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.10-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.10-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.10-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.10-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sun Sep 13 2020 Peter Robinson <pbrobinson@fedoraproject.org> - 1.2.10-1
- Update to 1.2.10
- Build with guile 2.2

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.9-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.9-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.9-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 17 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.2.9-9
- Rebuild for readline 8.0

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.9-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.9-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.9-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.9-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.9-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.9-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Jan 12 2017 Igor Gnatenko <ignatenko@redhat.com> - 1.2.9-2
- Rebuild for readline 7.x

* Wed May 18 2016 Filipe Rosset <rosset.filipe@gmail.com> - 1.2.9-1
- Rebuilt for new upstream version 1.2.9, fixes rhbz #1126700

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.8-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Aug 23 2014 Stjepan Gros <stjepan.gros@gmail.com> - 1.2.8-1
- Bump to a new upstream version
- Removed format specifier patch as it is applied upstream
- Typo fix in the description

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.7-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.7-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed May 21 2014 Filipe Rosset <rosset.filipe@gmail.com> - 1.2.7-3
- Fixes rhbz #1048604 and #1037194 plus spec cleanup

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Tue Feb 26 2013 Stjepan Gros <stjepan.gros@gmail.com> - 1.2.7-1
- Bump to a new upstream version
- GCompletition is deprecated and disabled by default so a flag was added to enable it
- Removed TODO packaging

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.5-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.5-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.5-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Dec 06 2011 Adam Jackson <ajax@redhat.com> - 1.2.5-4
- Rebuild for new libpng

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sun Nov 15 2009 Stjepan Gros <stjepan.gros@gmail.com> - 1.2.5-2
- Added missing BR

* Sun Oct 18 2009 Stjepan Gros <stjepan.gros@gmail.com> - 1.2.5-1
- Updated to a new upstream version

* Wed Sep 16 2009 Stjepan Gros <stjepan.gros@gmail.com> - 1.2.4-2
- Added desktop file
- Changed licence from GPLv3 to GPLv3+
- Documentation and samples are now in separate package
- Removed unnecessary build requires

* Mon Dec 29 2008 Stjepan Gros <stjepan.gros@gmail.com> - 1.2.4-1
- Initial package
