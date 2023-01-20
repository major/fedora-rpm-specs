%global packname BiocIO
%global packver 1.6.0

Name:             R-%{packname}
Version:          %{packver}
Release:          2%{?dist}
Source0:          http://www.bioconductor.org/packages/release/bioc/src/contrib/%{packname}_%{packver}.tar.gz
License:          Artistic 2.0
BuildArch:        noarch
URL:              http://www.bioconductor.org/packages/release/bioc/html/%{packname}.html
Summary:          Standard Input and Output for Bioconductor Packages
BuildRequires:    R-devel >= 4.0, tetex-latex
BuildRequires:    R-BiocGenerics, R-S4Vectors-devel
BuildRequires:    R-methods, R-tools
# Not doing the Suggests because I don't want to chase them any deeper.

%description
Implements `import()` and `export()` standard generics for importing and
exporting biological data formats. `import()` supports whole-file as well as
chunk-wise iterative import. The `import()` interface optionally provides a
standard mechanism for 'lazy' access via `filter()` (on row or element-like
components of the file resource), `select()` (on column-like components of
the file resource) and `collect()`. The `import()` interface optionally
provides transparent access to remote (e.g. via https) as well as local
access. Developers can register a file extension, e.g., `.loom` for dispatch
from character-based URIs to specific `import()` / `export()` methods based on
classes representing file types, e.g., `LoomFile()`.

%prep
%setup -q -c -n %{packname}

%build

%install
mkdir -p %{buildroot}%{_datadir}/R/library
R CMD INSTALL %{packname} -l %{buildroot}%{_datadir}/R/library
# Clean up in advance of check
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css

%check
# Missing deps
# %%{_bindir}/R CMD check %%{packname}

%files
%dir %{_datadir}/R/library/%{packname}
%doc %{_datadir}/R/library/%{packname}/doc
%doc %{_datadir}/R/library/%{packname}/html
%{_datadir}/R/library/%{packname}/DESCRIPTION
%{_datadir}/R/library/%{packname}/INDEX
%{_datadir}/R/library/%{packname}/NAMESPACE
%{_datadir}/R/library/%{packname}/help
%{_datadir}/R/library/%{packname}/Meta
%{_datadir}/R/library/%{packname}/R

%changelog
* Wed Jan 18 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Sep  3 2022 Tom Callaway <spot@fedoraproject.org> - 1.6.0-1
- update to 1.6.0
- rebuild for R 4.2.1

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jun 16 2021 Tom Callaway <spot@fedoraproject.org> - 1.2.0-1
- new package
