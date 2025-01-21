Name:           tinyxpath
Version:        1.3.1
Release:        24%{?dist}
Summary:        Small XPath syntax decoder

License:        zlib
URL:            http://tinyxpath.sourceforge.net/
Source0:        http://downloads.sourceforge.net/%{name}/%{name}_1_3_1.zip
# tinyxpath include a bundled version of tinyxml
Patch0:         %{name}.remove_bundled_tinyxml.patch
# Fix false-positive of the binary test (see https://sourceforge.net/p/tinyxpath/support-requests/7/ )
Patch1:         %name.fix_test.patch

BuildRequires: make
BuildRequires:  gcc-c++
BuildRequires:  tinyxml-devel autoconf automake
BuildRequires:  gcc

%description
TinyXPath is a small footprint XPath syntax decoder, written in C++.
- Syntax decoding
- Application to a TinyXML tree
- Function to extract a result from a tree (string, node set or integer)

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       tinyxml-devel

%description    devel
The %{name}-devel package contains library and header files for
developing applications that use %{name}.


%prep
%setup -q -c %{name}-%{version}
%patch -P0
%patch -P1
rm -rf tinyxml* tinystr*

# Correct some errors due to bundled tinyxml
sed -i 's+TiXmlNode::+TiXmlNode::TINYXML_+g' *.cpp
sed -i 's+#include "tinystr.h"+//#include "tinystr.h"+g' *.h

# Fix wrong EOF encoding
sed -i 's/\r$//' AUTHORS


%build
make -f Makefile.configure
# Build with -fPIC for the library
%configure CPPFLAGS="-fPIC"
make %{?_smp_mflags}

# Not really designed to be build as lib, DYI
g++ $RPM_OPT_FLAGS -shared -o lib%{name}.so.0.1 \
   -Wl,-soname,lib%{name}.so.0.1 `ls *.o | grep -v main.o` -ltinyxml


%check
./tinyxpath
BEFORE=($(grep "<tr><td>" out.htm | sed 's~<td>~_~' | sed 's~</td><td>~_~g' | sed 's~</td></tr>~~' | cut -d '_' -f 3))
AFTER=($(grep "<tr><td>" out.htm | sed 's~<td>~_~' | sed 's~</td><td>~_~g' | sed 's~</td></tr>~~' | cut -d '_' -f 4))
COUNT=0
TOTAL=$(grep "<tr><td>" out.htm | sed 's~<td>~_~' | sed 's~</td><td>~_~g' | sed 's~</td></tr>~~' | cut -d '_' -f 3 | wc -l)
while [ $COUNT -lt $TOTAL ]; do
  if [ -z "${AFTER[$COUNT]}" ] || [ "${AFTER[$COUNT]}" != "${BEFORE[$COUNT]}" ]
  then
    echo "Before: ${BEFORE[$COUNT]} After: ${AFTER[$COUNT]}"
    false
    break
  fi
  COUNT=$(($COUNT + 1))
done


%install
%make_install

# Install headers by hands.
mkdir -p %{buildroot}%{_includedir}/%{name}
install -pDm644 *.h %{buildroot}%{_includedir}/%{name}

#Install lib by hands.
mkdir -p %{buildroot}%{_libdir}
install -m 755 lib%{name}.so.0.1 %{buildroot}%{_libdir}
ln -s lib%{name}.so.0.1 %{buildroot}%{_libdir}/lib%{name}.so.0
ln -s lib%{name}.so.0.1 %{buildroot}%{_libdir}/lib%{name}.so

%ldconfig_scriptlets


%files
# Exclude binary, whicih is only for test
%exclude %{_bindir}/tinyxpath

%doc AUTHORS
%{_libdir}/lib%{name}.so.0
%{_libdir}/lib%{name}.so.0.*

%files devel
%{_includedir}/%{name}
%{_libdir}/lib%{name}.so


%changelog
* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Dec 10 2018 Michael Cronenworth <mike@cchtml.com> - 1.3.1-11
- Fix tests

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Mar 07 2018 Alexandre Moine <nobrakal@fedoraproject.org> - 1.3.1-9
- Add gcc as a build dependency.

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jul 31 2015 Alexandre Moine <nobrakal@gmail.com> 1.3.1-3
- Add tinyxml-devel as a Requires for tinyxpath-devel
- Remove by-hands installation of AUTHORS

* Thu Jul 30 2015 Alexandre Moine <nobrakal@gmail.com> 1.3.1-2
- Remove wrong license link
- Add AUTHORS to %%doc
- Exclude %%{_bindir}/tinyxpath beceause it is not useful
- Remove explicit dependency tinyxml
- Change soname to libtinyxpath.so.0.1 

* Tue Jul 14 2015 Alexandre Moine <nobrakal@gmail.com> 1.3.1-1
- Initial spec
