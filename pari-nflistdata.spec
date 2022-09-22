# md5sum is given on the download page
%global md5sum  227029dc39aea52bbf7909fb47583798

Name:           pari-nflistdata
Version:        20220326
Release:        2%{?dist}
Summary:        PARI/GP Computer Algebra System nflist extensions
License:        GPLv2+
URL:            https://pari.math.u-bordeaux.fr/packages.html
Source0:        https://pari.math.u-bordeaux.fr/pub/pari/packages/nflistdata.tgz

BuildArch:      noarch

%description
This package is needed by nflist to list fields of small discriminant
(currently needed by the single Galois group A5) or to list most regular
extensions of Q(T) in degree larger than 7.

%prep
# Verify the source file
test $(md5sum %{SOURCE0} | cut -d' ' -f1) = %{md5sum}

%autosetup -n data

# We'll ship the README as %%doc
mv nflistdata/README .

%build
# Nothing to do

%install
mkdir -p %{buildroot}%{_datadir}/pari
cp -a nflistdata %{buildroot}%{_datadir}/pari

%files
%doc README
%{_datadir}/pari/

%changelog
* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 20220326-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Mar 28 2022 Jerry James <loganjerry@gmail.com> - 20220326-1
- Version 20220326

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 20210527-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Aug 11 2021 Jerry James <loganjerry@gmail.com> - 20210527-1
- Initial RPM
