%global srcname streamlink
%global _description %{expand:Streamlink is a command-line utility that pipes video streams from various
services into a video player, such as VLC. The main purpose of Streamlink is to
allow the user to avoid buggy and CPU heavy flash plugins but still be able to
enjoy various streamed content. There is also an API available for developers
who want access to the video stream data. This project was forked from
Livestreamer, which is no longer maintained.}

Name:           python-%{srcname}
Version:        6.11.0
Release:        2%{?dist}
Summary:        Python library for extracting streams from various websites

# src/streamlink/packages/requests_file.py is Apache-2.0
License:        BSD-2-Clause AND Apache-2.0
URL:            https://streamlink.github.io/
Source0:        %{pypi_source %{srcname}}
# Fix documentation build
Patch1:         %{name}-6.6.2-documentation.patch
BuildRequires:  make
BuildRequires:  python3-devel
BuildRequires:  %{py3_dist shtab}
BuildArch:      noarch

%description
%{_description}


%package -n python3-%{srcname}
Summary:        %{summary}
Provides:       %{srcname} = %{version}-%{release}
# src/streamlink/packages/requests_file.py is a bundled copy of
# https://pypi.org/project/requests-file/, but it seems to have been forked;
# the contents do not correspond exactly to any version from 1.0 to 1.5.1
Provides:       bundled(python3dist(requests-file))
Obsoletes:      %{name}-doc < 6.7.0-1
Recommends:     /usr/bin/ffmpeg

%description -n python3-%{srcname}
%{_description}


%package bash-completion
Summary:        Bash completion for %{srcname}
Requires:       %{name} = %{version}-%{release}
Requires:       bash-completion
Supplements:    (%{name} and bash-completion)

%description bash-completion
Bash command line completion support for %{srcname}.


%package zsh-completion
Summary:        Zsh completion for %{srcname}
Requires:       %{name} = %{version}-%{release}
Requires:       zsh
Supplements:    (%{name} and zsh)

%description zsh-completion
Zsh command line completion support for %{srcname}.


%prep
%autosetup -n %{srcname}-%{version} -p1

# Fix dependency on pycryptodomex
sed -i -e 's/pycryptodome\b/&x/g' pyproject.toml

# Drop development dependencies not available in Fedora or not useful for tests
sed -i -e '/# code-linting/,/^$/d' -e '/# typing/,/^$/d' dev-requirements.txt
sed -i -e '/# typing/,/^$/d' -e '/^furo\b/d' -e 's/^\(sphinx-design\)\b.*/\1/' docs-requirements.txt


%generate_buildrequires
%pyproject_buildrequires -r docs-requirements.txt dev-requirements.txt


%build
%pyproject_wheel

# Generate man pages
PYTHONPATH=$PWD/src %make_build -C docs/ man SPHINXOPTS=-j%{?_smp_build_ncpus}
# Generate shell completion files
PYTHONPATH=$PWD/src ./script/build-shell-completions.sh


%install
%pyproject_install
%pyproject_save_files %{srcname} %{srcname}_cli

# Install man page
install -Dpm 0644 docs/_build/man/%{srcname}.1 $RPM_BUILD_ROOT%{_mandir}/man1/%{srcname}.1
# Install shell completion files
install -Dpm 0644 -t $RPM_BUILD_ROOT%{bash_completions_dir} completions/bash/%{srcname}
install -Dpm 0644 -t $RPM_BUILD_ROOT%{zsh_completions_dir} completions/zsh/_%{srcname}


%check
# Disable non-critical test failing on Python 3.13
%pytest -k "not test_datefmt_custom"


%files -n python3-%{srcname} -f %{pyproject_files}
%doc README.md
%license LICENSE
%{_bindir}/%{srcname}
%{_mandir}/man1/%{srcname}.1.*


%files bash-completion
%{_datadir}/bash-completion/completions/%{srcname}


%files zsh-completion
%{_datadir}/zsh/site-functions/_%{srcname}


%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 6.11.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Sun Oct 13 2024 Mohamed El Morabity <melmorabity@fedoraproject.org> - 6.11.0-1
- Update to 6.11.0

* Thu Aug 22 2024 Mohamed El Morabity <melmorabity@fedoraproject.org> - 6.9.0-1
- Update to 6.9.0

* Mon May 13 2024 Mohamed El Morabity <melmorabity@fedoraproject.org> - 6.7.4-1
- Update to 6.7.4

* Sun Mar 10 2024 Mohamed El Morabity <melmorabity@fedoraproject.org> - 6.7.0-1
- Update to 6.7.0
- Add proper requests-file bundling (thanks to Benjamin Beasley)
- Drop documentation package (thanks to Benjamin Beasley)
- Improve completion snippets installation (thanks to Benjamin Beasley)

* Sat Mar 02 2024 Mohamed El Morabity <melmorabity@fedoraproject.org> - 6.6.2-1
- Update to 6.6.2

* Wed Jan 31 2024 Mohamed El Morabity <melmorabity@fedoraproject.org> - 6.5.1-1
- Update to 6.5.1

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 6.4.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 6.4.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Nov 29 2023 Mohamed El Morabity <melmorabity@fedoraproject.org> - 6.4.2-1
- Update to 6.4.2

* Sat Nov 25 2023 Mohamed El Morabity <melmorabity@fedoraproject.org> - 6.4.1-1
- Update to 6.4.1

* Sun Oct 29 2023 Mohamed El Morabity <melmorabity@fedoraproject.org> - 6.3.1-1
- Update to 6.3.1

* Wed Oct 25 2023 Mohamed El Morabity <melmorabity@fedoraproject.org> - 6.3.0-1
- Update to 6.3.0

* Sun Oct 15 2023 Mohamed El Morabity <melmorabity@fedoraproject.org> - 6.2.1-1
- Update to 6.2.1

* Sun Sep 24 2023 Mohamed El Morabity <melmorabity@fedoraproject.org> - 5.5.1-4
- Fix RHBZ #2220526

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 5.5.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sun Jul 16 2023 Python Maint <python-maint@redhat.com> - 5.5.1-2
- Rebuilt for Python 3.12

* Sun May 21 2023 Mohamed El Morabity <melmorabity@fedoraproject.org> - 5.5.1-1
- Update to 5.5.1

* Sat Apr 08 2023 Mohamed El Morabity <melmorabity@fedoraproject.org> - 5.3.1-2
- Fix RHBZ #2185401 (switch to Font Awesome 6)

* Sun Mar 26 2023 Mohamed El Morabity <melmorabity@fedoraproject.org> - 5.3.1-1
- Update to 5.3.1

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 5.1.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jan 07 2023 Mohamed El Morabity <melmorabity@fedoraproject.org> - 5.1.2-1
- Update to 5.1.2

* Fri Dec 02 2022 Mohamed El Morabity <melmorabity@fedoraproject.org> - 5.1.1-1
- Update to 5.1.1

* Mon Nov 21 2022 Mohamed El Morabity <melmorabity@fedoraproject.org> - 5.1.0-1
- Update to 5.1.0
- Switch license tag to SPDX
- Fix RHBZ #2142098

* Mon Oct 10 2022 Mohamed El Morabity <melmorabity@fedoraproject.org> - 5.0.1-2
- Fix Recommends on ffmpeg

* Tue Sep 27 2022 Mohamed El Morabity <melmorabity@fedoraproject.org> - 5.0.1-1
- Update to 5.0.1

* Tue Aug 16 2022 Mohamed El Morabity <melmorabity@fedoraproject.org> - 4.3.0-1
- Update to 4.3.0

* Tue Aug 09 2022 Mohamed El Morabity <melmorabity@fedoraproject.org> - 4.2.0-1
- Update to 4.2.0

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jul 04 2022 Python Maint <python-maint@redhat.com> - 3.2.0-2
- Rebuilt for Python 3.11

* Tue Mar 08 2022 Mohamed El Morabity <melmorabity@fedoraproject.org> - 3.2.0-1
- Update to 3.2.0

* Tue Feb 01 2022 Mohamed El Morabity <melmorabity@fedoraproject.org> - 3.1.1-1
- Update to 3.1.1

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Sun Nov 21 2021 Mohamed El Morabity <melmorabity@fedoraproject.org> - 3.0.1-1
- Update to 3.0.1

* Wed Nov 17 2021 Mohamed El Morabity <melmorabity@fedoraproject.org> - 3.0.0-1
- Update to 3.0.0

* Tue Sep 07 2021 Mohamed El Morabity <melmorabity@fedoraproject.org> - 2.4.0-1
- Update to 2.4.0

* Mon Jul 26 2021 Mohamed El Morabity <melmorabity@fedoraproject.org> - 2.3.0-1
- Update to 2.3.0

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Sat Jun 19 2021 Mohamed El Morabity <melmorabity@fedoraproject.org> - 2.2.0-1
- Update to 2.2.0

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 2.1.2-2
- Rebuilt for Python 3.10

* Fri Jun 04 2021 Mohamed El Morabity <melmorabity@fedoraproject.org> - 2.1.2-1
- Update to 2.1.2

* Mon Apr 12 2021 Mohamed El Morabity <melmorabity@fedoraproject.org> - 2.1.1-1
- Update to 2.1.1

* Tue Mar 23 2021 Mohamed El Morabity <melmorabity@fedoraproject.org> - 2.1.0-1
- Update to 2.1.0

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jan 19 2021 Mohamed El Morabity <melmorabity@fedoraproject.org> - 2.0.0-1
- Update to 2.0.0

* Sun Oct 18 2020 Mohamed El Morabity <melmorabity@fedoraproject.org> - 1.7.0-1
- Update to 1.7.0

* Sun Sep 27 2020 Mohamed El Morabity <melmorabity@fedoraproject.org> - 1.6.0-2
- Fix dependency on pycryptodomex

* Thu Sep 24 2020 Mohamed El Morabity <melmorabity@fedoraproject.org> - 1.6.0-1
- Update to 1.6.0

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 07 2020 Mohamed El Morabity <melmorabity@fedoraproject.org> - 1.5.0-1
- Update to 1.5.0

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1.4.1-2
- Rebuilt for Python 3.9

* Mon May 11 2020 Mohamed El Morabity <melmorabity@fedoraproject.org> - 1.4.1-1
- Update to 1.4.1

* Tue Jan 28 2020 Mohamed El Morabity <melmorabity@fedoraproject.org> - 1.3.1-1
- Update to 1.3.1

* Tue Nov 26 2019 Mohamed El Morabity <melmorabity@fedoraproject.org> - 1.3.0-1
- Update to 1.3.0

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 1.2.0-3
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Wed Aug 21 2019 Miro Hrončok <mhroncok@redhat.com> - 1.2.0-2
- Rebuilt for Python 3.8

* Tue Aug 20 2019 Mohamed El Morabity <melmorabity@fedoraproject.org> - 1.2.0-1
- Update to 1.2.0
- Use pycryptodomex library instead of crypto

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 1.1.1-3
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Apr 03 2019 Mohamed El Morabity <melmorabity@fedoraproject.org> - 1.1.1-1
- Update to 1.1.1

* Sun Mar 31 2019 Mohamed El Morabity <melmorabity@fedoraproject.org> - 1.1.0-1
- Update to 1.1.0

* Mon Feb 04 2019 Mohamed El Morabity <melmorabity@fedoraproject.org> - 1.0.0-1
- Update to 1.0.0

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.14.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jan 11 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.14.2-5
- Enable python dependency generator

* Fri Oct 12 2018 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 0.14.2-4
- Python2 binary package has been removed
  See https://fedoraproject.org/wiki/Changes/Mass_Python_2_Package_Removal

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.14.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Jul 02 2018 Miro Hrončok <mhroncok@redhat.com> - 0.14.2-2
- Rebuilt for Python 3.7

* Mon Jul 02 2018 Mohamed El Morabity <melmorabity@fedoraproject.org> - 0.14.2-1
- Update to 0.14.2

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 0.13.0-2
- Rebuilt for Python 3.7

* Thu Jun 07 2018 Mohamed El Morabity <melmorabity@fedoraproject.org> - 0.13.0-1
- Update to 0.13.0

* Mon May 07 2018 Mohamed El Morabity <melmorabity@fedoraproject.org> - 0.12.1-1
- Update to 0.12.1

* Mon May 07 2018 Mohamed El Morabity <melmorabity@fedoraproject.org> - 0.12.0-1
- Update to 0.12.0

* Thu Mar 08 2018 Mohamed El Morabity <melmorabity@fedoraproject.org> - 0.11.0-1
- Update to 0.11.0

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Jan 30 2018 Iryna Shcherbina <ishcherb@redhat.com> - 0.10.0-2
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Wed Jan 24 2018 Mohamed El Morabity <melmorabity@fedoraproject.org> - 0.10.0-1
- Update to 0.10.0

* Tue Nov 14 2017 Mohamed El Morabity <melmorabity@fedoraproject.org> - 0.9.0-1
- Update to 0.9.0

* Tue Oct 10 2017 Mohamed El Morabity <melmorabity@fedoraproject.org> - 0.8.1-3
- Fix dependecy on python-websocket-client package

* Tue Sep 19 2017 Mohamed El Morabity <melmorabity@fedoraproject.org> - 0.8.1-2
- Add missing dependecy on python-websocket-client package

* Tue Sep 19 2017 Mohamed El Morabity <melmorabity@fedoraproject.org> - 0.8.1-1
- Update to 0.8.1

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Jun 30 2017 Mohamed El Morabity <melmorabity@fedoraproject.org> - 0.7.0-1
- Update to 0.7.0

* Thu May 11 2017 Mohamed El Morabity <melmorabity@fedoraproject.org> - 0.6.0-1
- Update to 0.6.0

* Wed Apr 05 2017 Mohamed El Morabity <melmorabity@fedoraproject.org> - 0.5.0-1
- Update to 0.5.0

* Fri Mar 10 2017 Mohamed El Morabity <melmorabity@fedoraproject.org> - 0.4.0-1
- Update to 0.4.0

* Wed Feb 22 2017 Mohamed El Morabity <melmorabity@fedoraproject.org> - 0.3.2-1
- Update to 0.3.2

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Jan 26 2017 Mohamed El Morabity <melmorabity@fedoraproject.org> - 0.3.0-1
- Update to 0.3.0

* Sat Jan 07 2017 Mohamed El Morabity <melmorabity@fedoraproject.org> - 0.2.0-3
- Add license to doc subpackage

* Sat Jan 07 2017 Mohamed El Morabity <melmorabity@fedoraproject.org> - 0.2.0-2
- Fix license tag
- Move documentation to a subpackage
- Enable tests

* Sun Dec 18 2016 Mohamed El Morabity <melmorabity@fedoraproject.org> - 0.2.0-1
- Update to 0.2.0

* Fri Dec 16 2016 Mohamed El Morabity <melmorabity@fedoraproject.org> - 0.1.0-1
- Initial RPM release
