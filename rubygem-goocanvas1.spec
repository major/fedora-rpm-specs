%global	gem_name	goocanvas

%global	glibminver	2.0.0
%global	gtkminver	2.0.0

# Basically rubygems supports installation of multiple versions,
# (with gem "goocanvas", "~> 1.2"), so keep the original
# %%{gem_name} as much as possible - except for
# pkgconfig file

Summary:	Ruby binding of GooCanvas
Name:		rubygem-%{gem_name}1
Version:	1.2.6
Release:	36%{?dist}
# from README	LGPL-2.1-only
# overall:	LGPL-2.1-or-later
# some files under sample/		GPL-2.0-or-later
# SPDX confirmed
License:	LGPL-2.1-or-later AND LGPL-2.1-only
URL:		http://ruby-gnome2.sourceforge.jp/
Source0:	https://rubygems.org/gems/%{gem_name}-%{version}.gem
# Licenses
# https://raw.github.com/ruby-gnome2/ruby-gnome2/master/COPYING.LIB
Source1:	COPYING.LIB.rubygem-goocanvas1
# http://www.gnu.org/licenses/gpl-2.0.txt
Source2:	COPYING.GPL.rubygem-goocanvas1
# New gdk_pixbuf 3.0.9 removes this definition
Patch0:	rubygem-goocanvas1-1.2.6-implicit-by-new-pixbuf.patch

# CRuby only
Requires:	ruby
BuildRequires:	ruby

BuildRequires:	gcc
BuildRequires:	rubygems-devel
BuildRequires:	rubygem-cairo-devel
BuildRequires:	rubygem-gtk2-devel >= %{gtkminver}
BuildRequires:	rubygem-gdk_pixbuf2 >= %{gtkminver}
BuildRequires:	ruby-devel
BuildRequires:	goocanvas-devel
Requires:	ruby(rubygems)
Provides:	rubygem(%{gem_name}) = %{version}-%{release}

%description
Ruby/GooCanvas is a Ruby binding of GooCanvas.

%package	doc
Summary:	Documentation for %{name}
# sample/demo.rb is under GPL-2.0-or-later
License:	LGPL-2.1-or-later AND LGPL-2.1-only AND GPL-2.0-or-later
Requires:	%{name}%{?_isa} = %{version}-%{release}

%description	doc
This package contains documentation for %{name}.

%package	devel
Summary:	Ruby/GooCanvas development environment
Requires:	%{name}%{?_isa} = %{version}-%{release}

%description devel
Header files and libraries for building a extension library for the
rubygem-%{gem_name}

%prep
%setup -q -n %{gem_name}-%{version}
mv ../%{gem_name}-%{version}.gemspec .

%patch -P0 -p1 -b .pixbuf

# For rubygem-glib 2.0.x
sed -i \
	-e 's|GLib.prepend_environment_path|GLib.prepend_dll_path|' \
	lib/goocanvas.rb \
	sample/goocanvas-gi.rb

# Kill shebang
grep -rl '#!.*/usr/bin' sample | \
	xargs sed -i -e '\@#![ ]*/usr/bin@d'
find sample/ -name \*.rb | xargs chmod 0644

# For rubygem(gdk_pixbuf2) >= 3.0.7
pushd ext/%{gem_name}
grep -l "rbgdk-pixbuf\.h" *.c *.h | \
	xargs sed -i '\@include.*rbgdk-pixbuf\.h@d'
popd

%build
export CONFIGURE_ARGS="--with-cflags='%{optflags}'"
export CONFIGURE_ARGS="$CONFIGURE_ARGS --with-pkg-config-dir=$(pwd)%{_libdir}/pkgconfig"

gem build %{gem_name}-%{version}.gemspec
%gem_install

%install
# Once copy all
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
	%{buildroot}%{gem_dir}/

# move header files, C extension files to the correct directory
mkdir -p %{buildroot}%{gem_extdir_mri}
cp -a ./%{gem_extdir_mri}/* %{buildroot}%{gem_extdir_mri}/

pushd %{buildroot}
rm -f .%{gem_extdir_mri}/{gem_make.out,mkmf.log}
popd

# move pkgconfig file
# And rename this one (to avoid name conflict
# from rubygem-goocanvas)
mkdir %{buildroot}%{_libdir}/pkgconfig
install -cpm 644 ./%{_libdir}/pkgconfig/*.pc \
	%{buildroot}%{_libdir}/pkgconfig/ruby-%{gem_name}1.pc

# Cleanups
rm -f %{buildroot}%{gem_cache}
pushd %{buildroot}%{gem_instdir}
rm -rf \
	Rakefile \
	ext/ \
	extconf.rb \
	*.gemspec \
	%{nil}
popd

# Licenses
for f in %{SOURCE1} %{SOURCE2}
do
	install -cpm 644 $f %{buildroot}%{gem_instdir}/$(basename $f | sed -e 's|\.%{name}||')
done

%check
# Currently no testsuite available

%files
%dir	%{gem_instdir}
%dir	%{gem_instdir}/lib/

%license	%{gem_instdir}/COPYING*
%doc	%{gem_instdir}/[D-Z]*

%{gem_instdir}/lib/%{gem_name}.rb
%{gem_extdir_mri}/

%{gem_spec}

%files	devel
%{_libdir}/pkgconfig/ruby-%{gem_name}1.pc

%files	doc
%{gem_docdir}/
%{gem_instdir}/sample/

%changelog
* Thu Jan 11 2024 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1.2.6-36
- SPDX migration

* Wed Jan 03 2024 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1.2.6-35
- Rebuild for https://fedoraproject.org/wiki/Changes/Ruby_3.3

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.6-34
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.6-33
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Jan 04 2023 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1.2.6-32
- Rebuild for https://fedoraproject.org/wiki/Changes/Ruby_3.2

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.6-31
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 27 2022 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1.2.6-30
- F-36: rebuild against ruby31

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.6-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.6-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.6-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jan 06 2021 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1.2.6-26
- F-34: rebuild against ruby 3.0

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.6-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.6-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jan 17 2020 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1.2.6-22
- F-32: rebuild against ruby27

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.6-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.6-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Jan 21 2019 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1.2.6-19
- F-30: rebuild against ruby26

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.6-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.6-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sat Jan 20 2018 Björn Esser <besser82@fedoraproject.org> - 1.2.6-16
- Rebuilt for switch to libxcrypt

* Thu Jan 04 2018 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1.2.6-15
- F-28: rebuild for ruby25

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.6-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.6-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.6-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Jan 30 2017 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1.2.6-11
- F-26: restore removed definition by gdk_pixbuf 3.0.9

* Wed Jan 11 2017 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1.2.6-10
- F-26: rebuild for ruby24
- Fix build with newer rubygem(gdk_pixbuf2)

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.6-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jan 13 2016 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1.2.6-8
- F-24: rebuild against ruby23

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.6-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Jan 16 2015 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1.2.6-6
- F-22: Rebuild for ruby 2.2

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.6-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Mon Apr 21 2014 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1.2.6-3
- F-21: rebuild for ruby 2.1 / rubygems 2.2

* Fri Nov  1 2013 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1.2.6-2
- Incorporate comments on review request (bug 1025095)

* Thu Oct 31 2013 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1.2.6-1
- Initial package
