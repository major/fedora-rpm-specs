%global packname  fontawesome
%global rlibdir  %{_datadir}/R/library

Name:             R-%{packname}
Version:          0.5.1
Release:          8%{?dist}
Summary:          Easily work with 'Font Awesome' Icons
%if 0%{?fedora} > 38
License:          MIT
%else
# Font bits are OFL
# Rest is MIT
License:          MIT AND OFL-1.1-RFN
%endif
URL:              https://CRAN.R-project.org/package=%{packname}
Source0:          https://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz

# Here's the R view of the dependencies world:
# Depends:
# Imports: R-rlang >= 0.4.10, R-htmltools >= 0.5.1.1
# Suggests: R-covr, R-dplyr >= 1.0.8, R-knitr >= 1.31, R-testthat >= 3.0.0, R-rsvg
# LinkingTo:
# Enhances:

BuildArch:        noarch
Requires:         R-core
%if 0%{?fedora} > 38
Requires:         fontawesome-fonts-web
%else
# This package has a copy of the fontawesome free fonts v6
Provides:         bundled(fontawesome-fonts-web) = 6.4.0
%endif
BuildRequires:    R-devel
BuildRequires:    tex(latex)
BuildRequires:    tex(inconsolata.sty)
BuildRequires:    R-rlang >= 1.0.6
BuildRequires:    R-htmltools >= 0.5.1.1
# Suggests
BuildRequires:    R-dplyr >= 1.0.8
BuildRequires:    R-knitr >= 1.31
BuildRequires:    R-testthat >= 3.0.0
BuildRequires:    R-rsvg
# For the tests
BuildRequires:    glibc-langpack-en

%description
Easily and flexibly insert 'Font Awesome' icons into 'R Markdown' documents
and 'Shiny' apps. These icons can be inserted into HTML content through inline
'SVG' tags or 'i' tags. There is also a utility function for exporting 'Font
Awesome' icons as 'PNG' images for those situations where raster graphics are
needed.

%prep
%setup -q -c -n %{packname}

# it is easier without a covr BR
pushd %{packname}
sed -i 's/covr, //g' DESCRIPTION
popd

%build

%install
mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%if 0%{?fedora} > 38
# Unbundle the FontAwesome fonts
rm -fr %{buildroot}%{rlibdir}/%{packname}/fontawesome
ln -s ../../../fontawesome %{buildroot}%{rlibdir}/%{packname}
%endif

%check
%{_bindir}/R CMD check %{packname}

# This and the %%ghost entry in %%files can be removed when F43 reaches EOL
%pretrans -p <lua>
path = "%{rlibdir}/%{packname}/fontawesome"
st = posix.stat(path)
if st and st.type == "directory" then
  status = os.rename(path, path .. ".rpmmoved")
  if not status then
    suffix = 0
    while not status do
      suffix = suffix + 1
      status = os.rename(path .. ".rpmmoved", path .. ".rpmmoved." .. suffix)
    end
    os.rename(path, path .. ".rpmmoved")
  end
end

%files
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/html
%{rlibdir}/%{packname}/DESCRIPTION
%license %{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/help
%{rlibdir}/%{packname}/INDEX
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/apps
%{rlibdir}/%{packname}/fontawesome
%ghost %{rlibdir}/%{packname}/fontawesome.rpmmoved

%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Apr 25 2024 Iñaki Úcar <iucar@fedoraproject.org> - 0.5.1-6
- R-maint-sig mass rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Dec  4 2023 Jerry James <loganjerry@gmail.com> - 0.5.1-3
- Fix upgrade issue (bz 2252701)
- Add missing inconsolata BR

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri May 12 2023 Iñaki Úcar <iucar@fedoraproject.org> - 0.5.1-1
- Update to 0.5.1

* Fri Apr 21 2023 Iñaki Úcar <iucar@fedoraproject.org> - 0.3.0-4
- R-maint-sig mass rebuild

* Thu Mar 30 2023 Jerry James <loganjerry@gmail.com> - 0.3.0-3
- Unbundle the FontAwesome fonts for F39+
- Convert the License tag to SPDX
- BR the English langpack for the tests

* Wed Jan 18 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Sep  2 2022 Tom Callaway <spot@fedoraproject.org> - 0.3.0-1
- initial package
