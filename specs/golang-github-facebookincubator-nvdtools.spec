# Generated by go2rpm 1.2
%bcond_without check

# https://github.com/facebookincubator/nvdtools
%global goipath         github.com/facebookincubator/nvdtools
Version:                0.1.4

%gometa

%global common_summary %{expand: A collection of tools for working with National Vulnerability Database feeds}
%global common_description %{expand:
A set of tools to work with the feeds (vulnerabilities, CPE dictionary etc.)
distributed by National Vulnerability Database (NVD)}

%global golicenses      LICENSE
%global godocs          CODE_OF_CONDUCT.md CONTRIBUTING.md HOWTO.md README.md\\\
                        cmd/fireeye2nvd/README.md cmd/flexera2nvd/README.md\\\
                        cmd/idefense2nvd/README.md cmd/nvdsync/README.md\\\
                        cmd/rbs2nvd/README.md cmd/snyk2nvd/README.md\\\
                        cmd/vfeed2nvd/README.md cvss2/README.md\\\
                        cvss3/README.md\\\
                        vulndb/sqlutil/README.md

Name:           %{goname}
Release:        17%{?dist}
Summary:        %{common_summary}

# Upstream license specification: Apache-2.0
# Automatically converted from old format: ASL 2.0 - review is highly recommended.
License:        Apache-2.0
URL:            %{gourl}
Source0:        %{gosource}

# nvdtools segfaults on 32 bit architectures
# https://github.com/facebookincubator/nvdtools/issues/167
ExcludeArch:    i686 armv7hl

BuildRequires:  golang(github.com/BurntSushi/toml)
BuildRequires:  golang(github.com/dgrijalva/jwt-go)
BuildRequires:  golang(github.com/facebookincubator/flog)
BuildRequires:  golang(github.com/go-sql-driver/mysql)
BuildRequires:  golang(github.com/pkg/errors)
BuildRequires:  golang(github.com/spf13/cobra)
BuildRequires:  golang(github.com/spf13/pflag)
BuildRequires:  golang(golang.org/x/oauth2)
BuildRequires:  golang(golang.org/x/oauth2/clientcredentials)
BuildRequires:  golang(golang.org/x/sync/errgroup)

%if %{with check}
# Tests
BuildRequires:  golang(github.com/andreyvit/diff)
BuildRequires:  golang(github.com/stretchr/testify/assert)
%endif

%description
%{common_description}

%package -n    nvdtools
Summary:       %{common_summary}
%description -n nvdtools
%{common_description}

%gopkg

%prep
%goprep
for cmd in cmd/* cvss2 cvss3 vulndb/sqlutil; do
  if [ -f $cmd/README.md ]; then
    mv $cmd/README.md $cmd/$(basename $cmd).md
  fi
done

%build
for cmd in cmd/* vulndb/sqlutil/b64schema; do
  %gobuild -o %{gobuilddir}/bin/$(basename $cmd) %{goipath}/$cmd
done

%install
%gopkginstall
install -m 0755 -vd                     %{buildroot}%{_bindir}
install -m 0755 -vp %{gobuilddir}/bin/* %{buildroot}%{_bindir}/

%if %{with check}
%check
%gocheck
%endif

%files -n nvdtools
%license LICENSE
%doc CODE_OF_CONDUCT.md CONTRIBUTING.md HOWTO.md README.md
%doc cmd/*/*.md
%doc cvss2/cvss2.md
%doc cvss3/cvss3.md
%doc vulndb/sqlutil/sqlutil.md
%{_bindir}/*

%gopkgfiles

%changelog
* Wed Jul 23 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.4-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_43_Mass_Rebuild

* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.4-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Jul 24 2024 Miroslav Suchý <msuchy@redhat.com> - 0.1.4-15
- convert license to SPDX

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.4-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sun Feb 11 2024 Maxwell G <maxwell@gtmx.me> - 0.1.4-13
- Rebuild for golang 1.22.0

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.4-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jan 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.4-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.4-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.4-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Aug 10 2022 Maxwell G <gotmax@e.email> - 0.1.4-8
- Rebuild to fix FTBFS

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.4-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Tue Jul 19 2022 Maxwell G <gotmax@e.email> - 0.1.4-6
- Rebuild for CVE-2022-{1705,32148,30631,30633,28131,30635,30632,30630,1962} in
  golang

* Sat Jul 09 2022 Maxwell G <gotmax@e.email> - 0.1.4-5
- Rebuild for CVE-2022-{24675,28327,29526 in golang}

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jan  4 2021 Davide Cavalca <dcavalca@fedoraproject.org> - 0.1.4-1
- Initial package
