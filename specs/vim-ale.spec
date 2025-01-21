%global         upstream_name   ale
%global         vimfiles        %{_datadir}/vim/vimfiles
%global         nvimfiles       %{_datadir}/nvim/runtime

Name:           vim-%upstream_name
Version:        3.3.0
Release:        5%{?dist}
Summary:        Asynchronous Vim Lint Engine
# Automatically converted from old format: BSD - review is highly recommended.
License:        LicenseRef-Callaway-BSD

URL:            https://github.com/dense-analysis/ale
Source0:        https://github.com/dense-analysis/%upstream_name/archive/v%version/%upstream_name-%version.tar.gz

BuildArch:      noarch

Requires:       (vim-enhanced or vim-X11)


%define desc(n:) \
ALE (Asynchronous Lint Engine) is a plugin providing linting (syntax checking \
and semantic errors) in %{-n*} while you edit your text files, \
and acts as a Vim Language Server Protocol client. \
\
ALE makes use of NeoVim and Vim job control functions and timers to run \
linters on the contents of text buffers and return errors as text is changed \
in %{-n*}.  This allows for displaying warnings and errors in files being \
edited in %{-n*} before files have been saved back to a filesystem. \
\
In other words, this plugin allows you to lint while you type.


%description
%desc -n Vim


%package -n neovim-%upstream_name
Requires:       neovim
Summary:        Asynchronous NeoVim Lint Engine

%description -n neovim-%upstream_name
%desc -n NeoVim


%prep
%autosetup -p1 -n %upstream_name-%version


%install
for dest in %vimfiles %nvimfiles; do
mkdir -p %buildroot"$dest"
cp -r ale_linters %buildroot"$dest"
cp -r autoload %buildroot"$dest"
cp -r doc %buildroot"$dest"
cp -r ftplugin %buildroot"$dest"
cp -r plugin %buildroot"$dest"
cp -r rplugin %buildroot"$dest"
cp -r syntax %buildroot"$dest"
done


%define ale_files(d:) \
%license LICENSE \
%doc %{-d*}/doc/* \
%{-d*}/ale_linters \
%{-d*}/autoload/* \
%{-d*}/rplugin \
%{-d*}/plugin/* \
%{-d*}/ftplugin/* \
%{-d*}/syntax/* \

%files
%ale_files -d %vimfiles


%files -n neovim-%upstream_name
%ale_files -d %nvimfiles


%changelog
* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Sep 04 2024 Miroslav Suchý <msuchy@redhat.com> - 3.3.0-4
- convert license to SPDX

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jul 24 2023 Pavel Raiskup <praiskup@redhat.com> - 3.3.0-1
- new upstream release

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Sep 15 2022 Kir Kolyshkin <kolyshkin@gmail.com> - 3.2.0-1
- new upstream release, per release notes:
  https://github.com/dense-analysis/ale/releases/tag/v3.2.0

* Wed Sep 07 2022 Pavel Raiskup <praiskup@redhat.com> - 3.1.0-5
- depend on vim-X11 or vim-enhanced (rhbz#2114642)

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jun 22 2021 Pavel Raiskup <praiskup@redhat.com> - 3.1.0-1
- new upstream release, per release notes:
  https://github.com/dense-analysis/ale/releases/tag/v3.1.0

* Mon Nov 30 2020 Pavel Raiskup <praiskup@redhat.com> - 3.0.0-2
- make the plugin working with neovim, too

* Sun Oct 11 2020 Pavel Raiskup <praiskup@redhat.com> - 3.0.0-1
- preparations for a copr build

* Tue Apr 21 2020 Pavel Raiskup <praiskup@redhat.com> - 2.6.0-1
- initial packaging
