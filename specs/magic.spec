%undefine   __brp_mangle_shebangs

Name:		magic
Version:	8.3.515
Release:	2%{?dist}
Summary:	A very capable VLSI layout tool

# LICENSE: HPND-UC-export-US: https://gitlab.com/fedora/legal/fedora-license-data/-/issues/504
# calma/:  HPND-UC-export-US: https://gitlab.com/fedora/legal/fedora-license-data/-/issues/504
# bplane/bpBins.c and etc: TCL
# drc/DRCcif.c: HPND
# scmos/COPYRIGHT: NPND
# SPDX confirmed
License:	HPND-UC-export-US AND TCL AND HPND
URL:		http://opencircuitdesign.com/%{name}/index.html

Source:	http://opencircuitdesign.com/%{name}/archive/%{name}-%{version}.tgz
Source1:	%{name}.desktop
Source2:	%{name}.png
Patch1:	%{name}-7.4.35-64bit.patch

BuildRequires:	make
BuildRequires:	gcc

BuildRequires:	cairo-devel
BuildRequires:	libGL-devel
BuildRequires:	libGLU-devel
BuildRequires:	libGLw-devel
BuildRequires:	libXext-devel
BuildRequires:	libXi-devel
BuildRequires:	libXmu-devel
BuildRequires:	pkgconfig(tk) <= 8.999
BuildRequires:	m4
BuildRequires:	desktop-file-utils
%if 0%{?fedora}
BuildRequires:	zlib-devel
%endif

BuildRequires:	tcsh

Requires:	tcsh
# Special FEL Gnome/KDE menu structure
Requires:	electronics-menu

%description
Magic is a venerable VLSI layout tool. Magic VLSI remains
popular with universities and small companies.

Magic is widely cited as being the easiest tool to use for
circuit layout, even for people who ultimately rely on commercial
tools for their product design flow.

%package doc
Summary:	Documentation for magic, A very capable VLSI layout tool
Requires:	%{name} = %{version}-%{release}


%description doc
This package contains the documentation of magic in the postscript
and some tutorials.


%prep
# tarball includes unneeded symlink, so we firstly
# create a directory and expand tarball there.
%setup -q -T -c %{name}-%{version} -a 0
cd %{name}-%{version}

rm -rf readline
rm -rf risp

sed -i.cflags -e 's|CFLAGS=.*CFLAGS|:|' configure

sed -i.nocpp \
	scripts/configure.in scripts/configure \
	-e 's|-lstdc++||' \
	%{nil}

sed -i.arch scripts/defs.mak.in \
	-e 's|^INSTALL_LIBDIR.*$|INSTALL_LIBDIR\t=%{_libdir}|'

sed -i "s|/usr/local/bin/tclsh|%{_bindir}/tclsh|" tcltk/strip_reflibs.tcl
sed -i "s|package require -exact|package require|" tcltk/tkcon.tcl

%if "x%{?__isa_bits}" == "x64"
%patch -P 1 -p0 -b .64bit
%endif

# Doesn't seem to need these.
sed -i scripts/configure \
	-e 's| -lfontconfig -lfreetype||'

%global __global_cflags_orig %__global_cflags
%global __global_cflags %__global_cflags_orig -Werror=implicit-function-declaration -Werror=implicit-int

# Not C23 compliant yet
%global optflags_orig %optflags
%global optflags %optflags_orig -std=gnu17

%build
cd %{name}-%{version}

export WISH_EXE=%{_bindir}/wish
%configure \
	--with-tcl=%{_libdir} \
	--with-tk=%{_libdir} \
	--with-tcllibs=%{_libdir} \
	--with-tklibs=%{_libdir} \
	%{nil}

#%make %%{?_smp_mflags}
# Parallel make _silently_ fails
unlink commands/readline || :
make -j1 -k \
    UNUSED_MODULES=""

%install
cd %{name}-%{version}
make install \
	DESTDIR=%{buildroot} \
	INSTALL="%{__install} -c -p" \
	CP="%{__cp} -p"

desktop-file-install \
	--vendor "" \
	--dir %{buildroot}%{_datadir}/applications/ \
	%{SOURCE1}

# applying timestamps
cp -pr \
	README* \
	TODO \
	VERSION \
	scmos/ \
	..

cp -pr %{buildroot}%{_libdir}/%{name}/{doc/,tutorial} ..
rm -rf %{buildroot}%{_libdir}/%{name}/{doc/,tutorial}

rm -f doc/html/Makefile

chmod -x %{buildroot}%{_libdir}/%{name}/tcl/console.tcl

mkdir -p %{buildroot}%{_datadir}/icons/hicolor/128x128/apps/
install -cpm 0644 %{SOURCE2} \
	%{buildroot}%{_datadir}/icons/hicolor/128x128/apps/%{name}.png

# Remove manpage currently unused for TCL building
# to avoid file conflict (bug 1330507)
rm -f %{buildroot}%{_mandir}/man1/extcheck.1*

%files
%doc	README*
%doc	TODO
%doc	VERSION
%{_bindir}/%{name}
%{_bindir}/ext2sim
%{_bindir}/ext2spice

%dir	%{_libdir}/%{name}/
%dir	%{_libdir}/%{name}/tcl/
%{_libdir}/%{name}/sys/
%{_libdir}/%{name}/tcl/bitmaps/
%{_libdir}/%{name}/tcl/*tcl
%{_libdir}/%{name}/tcl/*.so
%{_libdir}/%{name}/tcl/magicdnull
%{_libdir}/%{name}/tcl/magicexec

%{_mandir}/man?/*
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/128x128/apps/%{name}.png

%files doc
%doc	doc/
%doc	tutorial/
%doc	scmos/

%changelog
* Fri Jan 31 2025 Mamoru TASAKA <mtasaka@fedoraproject.org> - 8.3.515-2
- Use tk8 explicitly

* Tue Jan 21 2025 Mamoru TASAKA <mtasaka@fedoraproject.org> - 8.3.515-1
- 8.3.515

* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 8.3.512-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jan 10 2025 Mamoru TASAKA <mtasaka@fedoraproject.org> - 8.3.512-2
- Use -std=gnu17 (instead of c11)

* Fri Jan 10 2025 Mamoru TASAKA <mtasaka@fedoraproject.org> - 8.3.512-1
- 8.3.512

* Sat Dec 28 2024 Mamoru TASAKA <mtasaka@fedoraproject.org> - 8.3.508-1
- 8.3.508

* Fri Dec 13 2024 Mamoru TASAKA <mtasaka@fedoraproject.org> - 8.3.505-1
- 8.3.505

* Fri Nov 29 2024 Mamoru TASAKA <mtasaka@fedoraproject.org> - 8.3.502-1
- 8.3.502

* Sat Nov 23 2024 Mamoru TASAKA <mtasaka@fedoraproject.org> - 8.3.501-1
- 8.3.501

* Thu Nov 14 2024 Mamoru TASAKA <mtasaka@fedoraproject.org> - 8.3.499-1
- 8.3.499

* Tue Nov 05 2024 Mamoru TASAKA <mtasaka@fedoraproject.org> - 8.3.498-1
- 8.3.498

* Sat Oct 12 2024 Mamoru TASAKA <mtasaka@fedoraproject.org> - 8.3.497-1
- 8.3.497

* Tue Oct 01 2024 Mamoru TASAKA <mtasaka@fedoraproject.org> - 8.3.492-1
- 8.3.492

* Fri Sep 20 2024 Mamoru TASAKA <mtasaka@fedoraproject.org> - 8.3.491-1
- 8.3.491

* Mon Sep 09 2024 Mamoru TASAKA <mtasaka@fedoraproject.org> - 8.3.490-1
- 8.3.490

* Thu Aug 22 2024 Mamoru TASAKA <mtasaka@fedoraproject.org> - 8.3.489-1
- 8.3.489

* Wed Aug 14 2024 Mamoru TASAKA <mtasaka@fedoraproject.org> - 8.3.488-1
- 8.3.488

* Mon Aug 05 2024 Mamoru TASAKA <mtasaka@fedoraproject.org> - 8.3.487-1
- 8.3.487

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 8.3.486-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Mon Jun 17 2024 Mamoru TASAKA <mtasaka@tbz.t-com.ne.jp> - 8.3.486-1
- 8.3.486

* Wed Jun 05 2024 Mamoru TASAKA <mtasaka@fedoraproject.org> - 8.3.485-1
- 8.3.485

* Fri May 24 2024 Mamoru TASAKA <mtasaka@fedoraproject.org> - 8.3.483-1
- 8.3.483

* Mon May 13 2024 Mamoru TASAKA <mtasaka@fedoraproject.org> - 8.3.482-1
- 8.3.482

* Sat May 04 2024 Mamoru TASAKA <mtasaka@fedoraproject.org> - 8.3.477-1
- 8.3.477

* Sun Apr 28 2024 Mamoru TASAKA <mtasaka@fedoraproject.org> - 8.3.471-2
- Update SPDX identifier

* Tue Apr 09 2024 Mamoru TASAKA <mtasaka@fedoraproject.org> - 8.3.471-1
- 8.3.471

* Fri Mar 29 2024 Mamoru TASAKA <mtasaka@fedoraproject.org> - 8.3.466-1
- 8.3.466

* Wed Mar 20 2024 Mamoru TASAKA <mtasaka@fedoraproject.org> - 8.3.465-1
- 8.3.465

* Mon Mar 11 2024 Mamoru TASAKA <mtasaka@fedoraproject.org> - 8.3.464-1
- 8.3.464

* Thu Feb 29 2024 Mamoru TASAKA <mtasaka@fedoraproject.org> - 8.3.463-1
- 8.3.463

* Wed Feb 21 2024 Mamoru TASAKA <mtasaka@fedoraproject.org> - 8.3.462-1
- 8.3.462

* Sun Feb 04 2024 Mamoru TASAKA <mtasaka@fedoraproject.org> - 8.3.460-1
- 8.3.460

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 8.3.456-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 8.3.456-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jan  6 2024 Mamoru TASAKA <mtasaka@fedoraproject.org> - 8.3.456-1
- 8.3.456

* Tue Dec 26 2023 Mamoru TASAKA <mtasaka@fedoraproject.org> - 8.3.454-1
- 8.3.454

* Sun Dec 10 2023 Mamoru TASAKA <mtasaka@fedoraproject.org> - 8.3.453-1
- 8.3.453

* Mon Nov 27 2023 Mamoru TASAKA <mtasaka@fedoraproject.org> - 8.3.451-1
- 8.3.451

* Tue Nov  7 2023 Mamoru TASAKA <mtasaka@fedoraproject.org> - 8.3.445-1
- 8.3.445

* Tue Oct 17 2023 Mamoru TASAKA <mtasaka@fedoraproject.org> - 8.3.439-1
- 8.3.439

* Sat Oct  7 2023 Mamoru TASAKA <mtasaka@fedoraproject.org> - 8.3.436-1
- 8.3.436

* Tue Sep 26 2023 Mamoru TASAKA <mtasaka@fedoraproject.org> - 8.3.433-1
- 8.3.433

* Thu Sep 14 2023 Mamoru TASAKA <mtasaka@fedoraproject.org> - 8.3.429-1
- 8.3.429

* Tue Aug 29 2023 Mamoru TASAKA <mtasaka@fedoraproject.org> - 8.3.426-1
- 8.3.426

* Thu Aug 17 2023 Mamoru TASAKA <mtasaka@fedoraproject.org> - 8.3.424-1
- 8.3.424

* Tue Aug  8 2023 Mamoru TASAKA <mtasaka@fedoraproject.org> - 8.3.423-1
- 8.3.423

* Fri Jul 28 2023 Mamoru TASAKA <mtasaka@fedoraproject.org> - 8.3.417-1
- 8.3.417

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 8.3.413-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Jul 12 2023 Mamoru TASAKA <mtasaka@fedoraproject.org> - 8.3.413-1
- 8.3.413

* Mon Jun 12 2023 Mamoru TASAKA <mtasaka@fedoraproject.org> - 8.3.402-1
- 8.3.402

* Mon May 29 2023 Mamoru TASAKA <mtasaka@fedoraproject.org> - 8.3.400-1
- 8.3.400

* Thu May  4 2023 Mamoru TASAKA <mtasaka@fedoraproject.org> - 8.3.397-1
- 8.3.397

* Fri Apr 14 2023 Mamoru TASAKA <mtasaka@fedoraproject.org> - 8.3.389-1
- 8.3.389
- SPDX migration

* Tue Mar 28 2023 Mamoru TASAKA <mtasaka@fedoraproject.org> - 8.3.388-1
- 8.3.388

* Mon Mar 20 2023 Mamoru TASAKA <mtasaka@fedoraproject.org> - 8.3.382-1
- 8.3.382

* Mon Mar  6 2023 Mamoru TASAKA <mtasaka@fedoraproject.org> - 8.3.373-1
- 8.3.373

* Sat Feb 25 2023 Mamoru TASAKA <mtasaka@fedoraproject.org> - 8.3.370-1
- 8.3.370

* Fri Feb 17 2023 Mamoru TASAKA <mtasaka@fedoraproject.org> - 8.3.366-1
- 8.3.366

* Sun Feb  5 2023 Mamoru TASAKA <mtasaka@fedoraproject.org> - 8.3.365-1
- 8.3.365

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 8.3.361-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sun Jan 15 2023 Mamoru TASAKA <mtasaka@fedoraproject.org> - 8.3.361-1
- 8.3.361

* Sat Dec 31 2022 Mamoru TASAKA <mtasaka@fedoraproject.org> - 8.3.358-1
- 8.3.358

* Fri Dec 23 2022 Mamoru TASAKA <mtasaka@fedoraproject.org> - 8.3.357-1
- 8.3.357

* Fri Dec  2 2022 Mamoru TASAKA <mtasaka@fedoraproject.org> - 8.3.348-1
- 8.3.348

* Wed Nov 23 2022 Mamoru TASAKA <mtasaka@fedoraproject.org> - 8.3.345-1
- 8.3.345

* Mon Nov  7 2022 Mamoru TASAKA <mtasaka@fedoraproject.org> - 8.3.335-1
- 8.3.335

* Sun Oct 30 2022 Mamoru TASAKA <mtasaka@fedoraproject.org> - 8.3.333-1
- 8.3.333

* Thu Oct  6 2022 Mamoru TASAKA <mtasaka@fedoraproject.org> - 8.3.328-1
- 8.3.328

* Sun Sep 18 2022 Mamoru TASAKA <mtasaka@fedoraproject.org> - 8.3.324-1
- 8.3.324

* Tue Sep  6 2022 Mamoru TASAKA <mtasaka@fedoraproject.org> - 8.3.321-1
- 8.3.321

* Fri Aug 26 2022 Mamoru TASAKA <mtasaka@fedoraproject.org> - 8.3.316-1
- 8.3.316

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 8.3.315-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jul  1 2022 Mamoru TASAKA <mtasaka@fedoraproject.org> - 8.3.315-1
- 8.3.315

* Sun Jun 19 2022 Mamoru TASAKA <mtasaka@fedoraproject.org> - 8.3.312-1
- 8.3.312

* Fri Jun  3 2022 Mamoru TASAKA <mtasaka@fedoraproject.org> - 8.3.308-1
- 8.3.308

* Tue May 17 2022 Mamoru TASAKA <mtasaka@fedoraproject.org> - 8.3.304-1
- 8.3.304

* Thu May  5 2022 Mamoru TASAKA <mtasaka@fedoraproject.org> - 8.3.298-1
- 8.3.298

* Tue Apr 19 2022 Mamoru TASAKA <mtasaka@fedoraproject.org> - 8.3.291-1
- 8.3.291

* Tue Apr  5 2022 Mamoru TASAKA <mtasaka@fedoraproject.org> - 8.3.286-1
- 8.3.286

* Wed Mar 16 2022 Mamoru TASAKA <mtasaka@fedoraproject.org> - 8.3.276-1
- 8.3.276

* Tue Mar  1 2022 Mamoru TASAKA <mtasaka@fedoraproject.org> - 8.3.274-1
- 8.3.274

* Sun Feb 20 2022 Mamoru TASAKA <mtasaka@fedoraproject.org> - 8.3.269-1
- 8.3.269

* Thu Feb 10 2022 Mamoru TASAKA <mtasaka@fedoraproject.org> - 8.3.266-1
- 8.3.266

* Sun Jan 30 2022 Mamoru TASAKA <mtasaka@fedoraproject.org> - 8.3.263-1
- 8.3.263

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 8.3.257-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Jan 18 2022 Mamoru TASAKA <mtasaka@fedoraproject.org> - 8.3.257-1
- 8.3.257

* Mon Jan 10 2022 Mamoru TASAKA <mtasaka@fedoraproject.org> - 8.3.253-1
- 8.3.253

* Thu Dec 30 2021 Mamoru TASAKA <mtasaka@fedoraproject.org> - 8.3.245-1
- 8.3.245

* Mon Dec 20 2021 Mamoru TASAKA <mtasaka@fedoraproject.org> - 8.3.241-1
- 8.3.241

* Fri Dec 10 2021 Mamoru TASAKA <mtasaka@fedoraproject.org> - 8.3.239-1
- 8.3.239

* Wed Dec  1 2021 Mamoru TASAKA <mtasaka@fedoraproject.org> - 8.3.233-1
- 8.3.233

* Fri Nov 19 2021 Mamoru TASAKA <mtasaka@fedoraproject.org> - 8.3.229-1
- 8.3.229

* Thu Nov 11 2021 Mamoru TASAKA <mtasaka@fedoraproject.org> - 8.3.225-1
- 8.3.225

* Sun Oct 31 2021 Mamoru TASAKA <mtasaka@fedoraproject.org> - 8.3.221-1
- 8.3.221

* Wed Oct 20 2021 Mamoru TASAKA <mtasaka@fedoraproject.org> - 8.3.220-1
- 8.3.220

* Tue Oct  5 2021 Mamoru TASAKA <mtasaka@fedoraproject.org> - 8.3.212-1
- 8.3.212

* Sun Sep 12 2021 Mamoru TASAKA <mtasaka@fedoraproject.org> - 8.3.205-1
- 8.3.205

* Fri Aug 27 2021 Mamoru TASAKA <mtasaka@fedoraproject.org> - 8.3.199-1
- 8.3.199

* Sun Aug  8 2021 Mamoru TASAKA <mtasaka@fedoraproject.org> - 8.3.196-1
- 8.3.196

* Thu Jul 29 2021 Mamoru TASAKA <mtasaka@fedoraproject.org> - 8.3.191-1
- 8.3.191

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 8.3.188-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Sun Jul 18 2021 Mamoru TASAKA <mtasaka@fedoraproject.org> - 8.3.188-1
- 8.3.188

* Fri Jul  9 2021 Mamoru TASAKA <mtasaka@fedoraproject.org> - 8.3.184-1
- 8.3.184

* Fri Jun 25 2021 Mamoru TASAKA <mtasaka@fedoraproject.org> - 8.3.182-1
- 8.3.182

* Thu May 13 2021 Mamoru TASAKA <mtasaka@fedoraproject.org> - 8.3.162-1
- 8.3.162

* Sat May  1 2021 Mamoru TASAKA <mtasaka@fedoraproject.org> - 8.3.160-1
- 8.3.160

* Fri Mar 26 2021 Mamoru TASAKA <mtasaka@fedoraproject.org> - 8.3.149-1
- 8.3.149

* Mon Mar  8 2021 Mamoru TASAKA <mtasaka@fedoraproject.org> - 8.3.138-1
- 8.3.138

* Thu Feb 25 2021 Mamoru TASAKA <mtasaka@fedoraproject.org> - 8.3.132-1
- 8.3.132

* Sun Feb 21 2021 Mamoru TASAKA <mtasaka@fedoraproject.org> - 8.3.130-1
- 8.3.130

* Tue Feb 16 2021 Mamoru TASAKA <mtasaka@fedoraproject.org> - 8.3.126-1
- 8.3.126

* Fri Feb  5 2021 Mamoru TASAKA <mtasaka@fedoraproject.org> - 8.3.124-1
- 8.3.124

* Thu Jan 28 2021 Mamoru TASAKA <mtasaka@fedoraproject.org> - 8.3.122-1
- 8.3.122

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 8.3.117-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jan 18 2021 Mamoru TASAKA <mtasaka@fedoraproject.org> - 8.3.117-1
- 8.3.117

* Fri Jan  8 2021 Mamoru TASAKA <mtasaka@fedoraproject.org> - 8.3.111-1
- 8.3.111

* Tue Dec 29 2020 Mamoru TASAKA <mtasaka@fedoraproject.org> - 8.3.105-1
- 8.3.105

* Sun Dec 20 2020 Mamoru TASAKA <mtasaka@fedoraproject.org> - 8.3.100-1
- 8.3.100

* Tue Dec  8 2020 Mamoru TASAKA <mtasaka@fedoraproject.org> - 8.3.92-1
- 8.3.92

* Wed Nov 25 2020 Mamoru TASAKA <mtasaka@fedoraproject.org> - 8.3.88-1
- 8.3.88

* Thu Nov  5 2020 Mamoru TASAKA <mtasaka@fedoraproject.org> - 8.3.76-1
- 8.3.76

* Tue Oct 27 2020 Mamoru TASAKA <mtasaka@fedoraproject.org> - 8.3.73-1
- 8.3.73

* Thu Oct 22 2020 Mamoru TASAKA <mtasaka@fedoraproject.org> - 8.3.71-1
- 8.3.71

* Sat Oct 17 2020 Mamoru TASAKA <mtasaka@fedoraproject.org> - 8.3.67-1
- 8.3.67

* Fri Oct  9 2020 Mamoru TASAKA <mtasaka@fedoraproject.org> - 8.3.63-1
- 8.3.63

* Wed Sep 30 2020 Mamoru TASAKA <mtasaka@fedoraproject.org> - 8.3.61-1
- 8.3.61

* Tue Sep  8 2020 Mamoru TASAKA <mtasaka@fedoraproject.org> - 8.3.54-1
- 8.3.54

* Fri Aug 28 2020 Mamoru TASAKA <mtasaka@fedoraproject.org> - 8.3.50-1
- 8.3.50

* Tue Aug 11 2020 Mamoru TASAKA <mtasaka@fedoraproject.org> - 8.3.49-1
- 8.3.49

* Fri Aug  7 2020 Mamoru TASAKA <mtasaka@fedoraproject.org> - 8.3.47-1
- 8.3.47

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 8.3.31-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jul  2 2020 Mamoru TASAKA <mtasaka@fedoraproject.org> - 8.3.31-1
- 8.3.31

* Fri Jun 12 2020 Mamoru TASAKA <mtasaka@fedoraproject.org> - 8.3.11-1
- 8.3.11

* Wed May  6 2020 Mamoru TASAKA <mtasaka@fedoraproject.org> - 8.3.5-1
- 8.3.5

* Thu Apr 02 2020 Björn Esser <besser82@fedoraproject.org> - 8.2.196-2
- Fix string quoting for rpm >= 4.16

* Tue Mar 17 2020 Mamoru TASAKA <mtasaka@fedoraproject.org> - 8.2.196-1
- 8.2.196

* Wed Mar 11 2020 Mamoru TASAKA <mtasaka@fedoraproject.org> - 8.2.194-1
- 8.2.194

* Fri Mar  6 2020 Mamoru TASAKA <mtasaka@fedoraproject.org> - 8.2.190-1
- 8.2.190

* Tue Feb 25 2020 Mamoru TASAKA <mtasaka@fedoraproject.org> - 8.2.186-1
- 8.2.186

* Tue Feb 18 2020 Mamoru TASAKA <mtasaka@fedoraproject.org> - 8.2.182-1
- 8.2.182

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 8.2.181-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Jan 27 2020 Mamoru TASAKA <mtasaka@fedoraproject.org> - 8.2.181-1
- 8.2.181

* Wed Jan 15 2020 Mamoru TASAKA <mtasaka@fedoraproject.org> - 8.2.178-1
- 8.2.178

* Mon Dec 30 2019 Mamoru TASAKA <mtasaka@fedoraproject.org> - 8.2.175-1
- 8.2.175

* Thu Dec 19 2019 Mamoru TASAKA <mtasaka@fedoraproject.org> - 8.2.174-1
- 8.2.174

* Mon Dec  9 2019 Mamoru TASAKA <mtasaka@fedoraproject.org> - 8.2.171-1
- 8.2.171

* Mon Nov 25 2019 Mamoru TASAKA <mtasaka@fedoraproject.org> - 8.2.167-1
- 8.2.167

* Fri Nov  8 2019 Mamoru TASAKA <mtasaka@fedoraproject.org> - 8.2.157-1
- 8.2.157

* Fri Oct 25 2019 Mamoru TASAKA <mtasaka@fedoraproject.org> - 8.2.151-1
- 8.2.151

* Tue Oct 15 2019 Mamoru TASAKA <mtasaka@fedoraproject.org> - 8.2.145-1
- 8.2.145

* Fri Sep 27 2019 Mamoru TASAKA <mtasaka@fedoraproject.org> - 8.2.142-1
- 8.2.142

* Wed Sep 11 2019 Mamoru TASAKA <mtasaka@fedoraproject.org> - 8.2.139-1
- 8.2.139

* Mon Sep  2 2019 Mamoru TASAKA <mtasaka@fedoraproject.org> - 8.2.138-1
- 8.2.138

* Fri Aug 23 2019 Mamoru TASAKA <mtasaka@fedoraproject.org> - 8.2.136-1
- 8.2.136

* Sun Aug 11 2019 Mamoru TASAKA <mtasaka@fedoraproject.org> - 8.2.134-1
- 8.2.134

* Tue Jul 30 2019 Mamoru TASAKA <mtasaka@fedoraproject.org> - 8.2.130-1
- 8.2.130

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 8.2.122-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Jul  9 2019 Mamoru TASAKA <mtasaka@fedoraproject.org> - 8.2.122-1
- 8.2.122

* Fri Jun 14 2019 Mamoru TASAKA <mtasaka@fedoraproject.org> - 8.2.120-1
- 8.2.120

* Fri Jun  7 2019 Mamoru TASAKA <mtasaka@fedoraproject.org> - 8.2.118-1
- 8.2.118

* Wed May 29 2019 Mamoru TASAKA <mtasaka@fedoraproject.org> - 8.2.115-1
- 8.2.115

* Wed May 22 2019 Mamoru TASAKA <mtasaka@fedoraproject.org> - 8.2.114-1
- 8.2.114

* Mon May 13 2019 Mamoru TASAKA <mtasaka@fedoraproject.org> - 8.2.113-1
- 8.2.113

* Fri Apr 12 2019 Mamoru TASAKA <mtasaka@fedoraproject.org> - 8.2.110-1
- 8.2.110

* Mon Apr  1 2019 Mamoru TASAKA <mtasaka@fedoraproject.org> - 8.2.102-1
- 8.2.102

* Mon Mar 18 2019 Mamoru TASAKA <mtasaka@fedoraproject.org> - 8.2.100-1
- 8.2.100

* Mon Feb 25 2019 Mamoru TASAKA <mtasaka@fedoraproject.org> - 8.2.99-1
- 8.2.99

* Mon Feb 11 2019 Mamoru TASAKA <mtasaka@fedoraproject.org> - 8.2.97-1
- 8.2.97

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 8.2.90-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jan  3 2019 Mamoru TASAKA <mtasaka@fedoraproject.org> - 8.2.90-1
- 8.2.90

* Sun Dec 30 2018 Mamoru TASAKA <mtasaka@fedoraproject.org> - 8.2.89-1
- 8.2.89

* Fri Dec 21 2018 Mamoru TASAKA <mtasaka@fedoraproject.org> - 8.2.88-1
- 8.2.88

* Sun Dec  9 2018 Mamoru TASAKA <mtasaka@fedoraproject.org> - 8.2.85-1
- 8.2.85

* Mon Dec  3 2018 Mamoru TASAKA <mtasaka@fedoraproject.org> - 8.2.84-1
- 8.2.84

* Wed Nov 21 2018 Mamoru TASAKA <mtasaka@fedoraproject.org> - 8.2.83-1
- 8.2.83

* Mon Nov 12 2018 Mamoru TASAKA <mtasaka@fedoraproject.org> - 8.2.79-1
- 8.2.79

* Fri Oct 26 2018 Mamoru TASAKA <mtasaka@fedoraproject.org> - 8.2.76-1
- 8.2.76

* Wed Oct  3 2018 Mamoru TASAKA <mtasaka@fedoraproject.org> - 8.2.74-1
- 8.2.74

* Tue Oct  2 2018 Mamoru TASAKA <mtasaka@fedoraproject.org> - 8.2.73-1
- 8.2.73

* Tue Sep 25 2018 Mamoru TASAKA <mtasaka@fedoraproject.org> - 8.2.72-1
- 8.2.72

* Mon Sep  3 2018 Mamoru TASAKA <mtasaka@fedoraproject.org> - 8.2.68-1
- 8.2.68

* Fri Aug 24 2018 Mamoru TASAKA <mtasaka@fedoraproject.org> - 8.2.66-1
- 8.2.66

* Tue Jul 31 2018 Florian Weimer <fweimer@redhat.com> - 8.2.65-2
- Rebuild with fixed binutils

* Mon Jul 30 2018 Mamoru TASAKA <mtasaka@fedoraproject.org> - 8.2.65-1
- 8.2.65

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 8.2.64-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Jun 28 2018 Mamoru TASAKA <mtasaka@fedoraproject.org> - 8.2.64-1
- 8.2.64

* Mon Jun 18 2018 Mamoru TASAKA <mtasaka@fedoraproject.org> - 8.2.62-1
- 8.2.62

* Wed May 30 2018 Mamoru TASAKA <mtasaka@fedoraproject.org> - 8.2.61-1
- 8.2.61

* Sun Apr 29 2018 Mamoru TASAKA <mtasaka@fedoraproject.org> - 8.2.60-1
- 8.2.60

* Mon Apr 16 2018 Mamoru TASAKA <mtasaka@fedoraproject.org> - 8.2.55-1
- 8.2.55

* Fri Apr  6 2018 Mamoru TASAKA <mtasaka@fedoraproject.org> - 8.2.54-1
- 8.2.54

* Tue Mar 27 2018 Mamoru TASAKA <mtasaka@fedoraproject.org> - 8.2.50-1
- 8.2.50

* Wed Mar  7 2018 Mamoru TASAKA <mtasaka@fedoraproject.org> - 8.2.47-1
- 8.2.47

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 8.2.46-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Feb  5 2018 Mamoru TASAKA <mtasaka@fedoraproject.org> - 8.2.46-1
- 8.2.46

* Thu Jan 18 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 8.2.39-2
- Remove obsolete scriptlets

* Thu Nov  2 2017 Mamoru TASAKA <mtasaka@fedoraproject.org> - 8.2.39-1
- 8.2.39

* Wed Oct 18 2017 Mamoru TASAKA <mtasaka@fedoraproject.org> - 8.2.38-1
- 8.2.38

* Tue Oct 10 2017 Mamoru TASAKA <mtasaka@fedoraproject.org> - 8.2.34-1
- 8.2.34

* Fri Oct  6 2017 Mamoru TASAKA <mtasaka@fedoraproject.org> - 8.2.31-1
- 8.2.31

* Fri Sep 29 2017 Mamoru TASAKA <mtasaka@fedoraproject.org> - 8.2.30-1
- 8.2.30

* Thu Sep 28 2017 Mamoru TASAKA <mtasaka@fedoraproject.org> - 8.2.29-1
- 8.2.29

* Mon Sep 25 2017 Mamoru TASAKA <mtasaka@fedoraproject.org> - 8.2.28-1
- 8.2.28

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 8.1.183-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Mon Jul 31 2017 Mamoru TASAKA <mtasaka@fedoraproject.org> - 8.1.183-1
- 8.1.183

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 8.1.180-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Jul 25 2017 Mamoru TASAKA <mtasaka@fedoraproject.org> - 8.1.180-1
- 8.1.180

* Tue Jul  4 2017 Mamoru TASAKA <mtasaka@fedoraproject.org> - 8.1.175-1
- 8.1.175

* Fri Jun 23 2017 Mamoru TASAKA <mtasaka@fedoraproject.org> - 8.1.172-1
- 8.1.172

* Fri Jun 16 2017 Mamoru TASAKA <mtasaka@fedoraproject.org> - 8.1.170-1
- 8.1.170

* Fri Jun 02 2017 Mamoru TASAKA <mtasaka@fedoraproject.org> - 8.1.168-1
- 8.1.168

* Mon May 15 2017 Mamoru TASAKA <mtasaka@fedoraproject.org> - 8.1.166-1
- 8.1.166

* Fri Apr 14 2017 Mamoru TASAKA <mtasaka@fedoraproject.org> - 8.1.158-1
- 8.1.158

* Mon Mar 13 2017 Mamoru TASAKA <mtasaka@fedoraproject.org> - 8.1.157-1
- 8.1.157

* Mon Feb 27 2017 Mamoru TASAKA <mtasaka@fedoraproject.org> - 8.1.153-1
- 8.1.153

* Thu Feb 16 2017 Mamoru TASAKA <mtasaka@fedoraproject.org> - 8.1.149-1
- 8.1.149

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 8.1.142-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb  2 2017 Mamoru TASAKA <mtasaka@fedoraproject.org> - 8.1.142-1
- 8.1.142

* Sun Jan 15 2017 Mamoru TASAKA <mtasaka@fedoraproject.org> - 8.1.135-1
- 8.1.135

* Thu Jan  5 2017 Mamoru TASAKA <mtasaka@fedoraproject.org> - 8.1.134-1
- 8.1.134

* Sun Jan  1 2017 Mamoru TASAKA <mtasaka@fedoraproject.org> - 8.1.132-1
- 8.1.132

* Sat Dec 31 2016 Mamoru TASAKA <mtasaka@fedoraproject.org> - 8.1.130-1
- 8.1.130

* Mon Dec 26 2016 Mamoru TASAKA <mtasaka@fedoraproject.org> - 8.1.127-1
- 8.1.127

* Fri Dec  2 2016 Mamoru TASAKA <mtasaka@fedoraproject.org> - 8.1.119-1
- 8.1.119

* Tue Nov 29 2016 Mamoru TASAKA <mtasaka@fedoraproject.org> - 8.1.118-1
- 8.1.118

* Sun Nov 20 2016 Mamoru TASAKA <mtasaka@fedoraproject.org> - 8.1.114-1
- 8.1.114

* Fri Nov 11 2016 Mamoru TASAKA <mtasaka@fedoraproject.org> - 8.1.113-1
- 8.1.113

* Mon Oct 24 2016 Mamoru TASAKA <mtasaka@fedoraproject.org> - 8.1.111-1
- 8.1.111

* Mon Oct 24 2016 Mamoru TASAKA <mtasaka@fedoraproject.org> - 8.1.110-1
- 8.1.110

* Fri Oct 14 2016 Mamoru TASAKA <mtasaka@fedoraproject.org> - 8.1.108-1
- 8.1.108

* Sun Sep 25 2016 Mamoru TASAKA <mtasaka@fedoraproject.org> - 8.1.107-1
- 8.1.107

* Fri Jul 29 2016 Mamoru TASAKA <mtasaka@fedoraproject.org> - 8.1.106-1
- 8.1.106

* Sat Jun 25 2016 Mamoru TASAKA <mtasaka@fedoraproject.org> - 8.1.104-1
- 8.1.104

* Wed May  4 2016 Mamoru TASAKA <mtasaka@fedoraproject.org> - 8.0.210-3
- Remove manpage currently unused for TCL building
  to avoid file conflict (bug 1330507)

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 8.0.210-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Oct 14 2015 Mamoru TASAKA <mtasaka@fedoraproject.org> - 8.0.210-1
- 8.0.210
- Remove unneeded lines from patches
- Correct license

* Fri Oct  9 2015 Mamoru TASAKA <mtasaka@fedoraproject.org> - 8.0.174-4
- Fix isa_bits conditional
- Patch for -Werror=format-security
- Build with -j1, parallel build currently fails

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 8.0.174-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 8.0.174-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Tue Jul  8 2014 Peter Robinson <pbrobinson@fedoraproject.org> 8.0.174-1
- 8.0.174 
- Generic 64bit platform detection

* Wed Jun 18 2014 Yaakov Selkowitz <yselkowi@redhat.com> - 8.0.60-9
- Fix FTBFS with -Werror=format-security (#1037190, #1106151)
- Apply 64bit patch on aarch64
- Cleanup spec

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 8.0.60-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed May 21 2014 Jaroslav Škarvada <jskarvad@redhat.com> - 8.0.60-7
- Rebuilt for https://fedoraproject.org/wiki/Changes/f21tcl86

* Wed Jul 31 2013 Ville Skyttä <ville.skytta@iki.fi> - 8.0.60-6
- Drop unneeded %%install doc dir creation.

* Tue Mar 16 2010 Thibault North <tnorth [AT] fedoraproject DOT org> - 8.0.60-1
- new upstream release with minor fixes

* Fri Aug 28 2009 Chitlesh Goorah <chitlesh [AT] fedoraproject DOT org> - 8.0.54-1
- new upstream release

* Wed Jan 07 2009 Chitlesh Goorah <chitlesh [AT] fedoraproject DOT org> - 7.5.169-1
- new upstream release
