%global         vimfiles        %{_datadir}/vim/vimfiles
%global         upstream_name   syntastic

%global         appdata_dir %{_datadir}/appdata
%global         python python3

Name:           vim-%{upstream_name}
Version:        3.10.0
Release:        25%{?dist}
Summary:        A vim plugins to check syntax for programming languages
Summary(fr):    Une extension de vim vérifiant la syntaxe pour les langages de programmation

License:        WTFPL
URL:            https://github.com/scrooloose/syntastic
Source0:        https://github.com/scrooloose/syntastic/archive/%{version}/%{upstream_name}-%{version}.tar.gz
Source1:        vim-syntastic.metainfo.xml

Patch0:         vim-syntastic-3.9.0-python3-shebang.patch
Patch1:         vim-syntastic-3.10.0-5-rvim.patch
Patch2:         vim-syntastic-3.10.0-yamllint-default.patch

BuildArch:      noarch
ExclusiveArch:  %{java_arches} noarch
Requires:       vim
BuildRequires:  glibc-common
# Needed for AppData check.
BuildRequires:  libappstream-glib
# Rename from 'syntastic'
Provides:       %upstream_name = %version-%release
Obsoletes:      %upstream_name < 3.7.0-6

# (temporarily?) dropped subpackages
Obsoletes:      %name-d < %version-%release
Obsoletes:      %name-lisp < %version-%release
Obsoletes:      %name-rnc < %version-%release
Obsoletes:      %name-go < %version-%release
Obsoletes:      %name-coffee < %version-%release
Obsoletes:      %name-scala < %version-%release

%description
Syntastic is a syntax checking plugin that runs files through external syntax
checkers and displays any resulting errors to the user. This can be done on
demand, or automatically as files are saved. If syntax errors are detected, the
user is notified and is happy because they didn't have to compile their code or
execute their script to find them.

%description -l fr
Syntastic est une extension vérifiant la syntaxe des fichiers source, un outil
externe de vérification affiche toutes les erreurs trouvées à l'utilisateur.
Ceci peut être fait à la demande ou automatique au moment de la sauvegarde
du fichier. Si une erreur de syntaxe est détecté, les utilisateurs sont
informés et sont heureux de ne pas avoir compiler leur code ou d'avoir
exécuter leur script afin de les trouver.


%define add_subpackage(n:)                                                          \
%package %{-n*}                                                                     \
Summary:        A syntax checker for %{-n*} programming language                    \
Summary(fr):    Un vérificateur de syntaxe pour le langage de programmation %{-n*}  \
Requires:       %{name} =  %{version}-%{release}                                    \
Requires:       %*                                                                  \
Provides:       %upstream_name-%{-n*} = %version-%release                           \
Obsoletes:      %upstream_name-%{-n*} < 3.7.0-6                                     \
%{expand:%%{?%{-n*}_avail_arches:ExclusiveArch: %%%{-n*}_avail_arches}}             \
%description %{-n*}                                                                 \
Allows checking %{-n*} sources files.                                               \
%description -l fr %{-n*}                                                           \
Permet de vérifier les fichiers sources écrit en %{-n*}.                            \
%global files_to_do %{?files_to_do}                                               \\\
%files_for_lang %{-n*}                                                            \\\
%{expand:%%{?additional_files_for_lang_%{-n*}}}


# Initialize files_to_do macro here to empty string.  FedoraReview tool, for
# example, runs 'rpm.TransactionSet().parseSpec("syntastic.spec")' _twice_,
# while global macros survive from the first call (we don't want to have all
# %%files sections generated twice).
%global files_to_do %nil
%add_subpackage -n ada gcc-gnat
%add_subpackage -n ansible ansible-lint
%add_subpackage -n asciidoc asciidoc %name-text
%add_subpackage -n asl acpica-tools
%add_subpackage -n asm nasm
%global additional_files_for_lang_c \
%{vimfiles}/autoload/syntastic/c.vim
%add_subpackage -n c gcc
%add_subpackage -n cabal cabal-install
# cofee-script has been retired
#%%add_subpackage -n coffee coffee-script
%add_subpackage -n coq coq
%add_subpackage -n cpp gcc-c++
%add_subpackage -n cs mono-core
%add_subpackage -n css csslint
%add_subpackage -n cucumber rubygem-cucumber
#https://pagure.io/packaging-committee/issue/312
#%%add_subpackage -n d ldc
%add_subpackage -n docbk /usr/bin/xmllint
%add_subpackage -n elixir elixir
%add_subpackage -n erlang erlang-erts
%add_subpackage -n eruby ruby
%add_subpackage -n fortran gcc-gfortran
%add_subpackage -n glsl mesa-libGLU
%add_subpackage -n go golang-bin
%add_subpackage -n haml rubygem-haml
%add_subpackage -n help proselint
%add_subpackage -n haskell ghc
%add_subpackage -n html sed curl tidy
%add_subpackage -n java java-devel
%add_subpackage -n json %{python}-demjson
%add_subpackage -n julia julia
%add_subpackage -n less nodejs
%add_subpackage -n lex flex
#https://pagure.io/packaging-committee/issue/312
#%%add_subpackage -n lisp clisp
%add_subpackage -n llvm llvm
%add_subpackage -n lua lua
%add_subpackage -n matlab octave
%add_subpackage -n nasm nasm
%add_subpackage -n objc gcc-objc
%add_subpackage -n objcpp gcc-objc++
%add_subpackage -n ocaml ocaml
%add_subpackage -n perl perl-interpreter %name-pod
%add_subpackage -n perl6 rakudo
%add_subpackage -n php php
%add_subpackage -n po gettext
%add_subpackage -n pod perl-interpreter
%add_subpackage -n puppet puppet
%add_subpackage -n python pylint /usr/bin/pyflakes
%add_subpackage -n qml /usr/bin/qmllint
#rnv has been retired
#%%add_subpackage -n rnc rnv
%add_subpackage -n rst %{python}-docutils %name-text %name-xml %name-docbk
%add_subpackage -n ruby ruby
%add_subpackage -n sass rubygem-sass
#Scala has been removed as of F42
#%%add_subpackage -n scala scala
%add_subpackage -n scss rubygem-sass
%add_subpackage -n sh bash
%add_subpackage -n spec rpmlint
%add_subpackage -n tcl tcl
%add_subpackage -n tex texlive-latex
%add_subpackage -n texinfo texinfo
%add_subpackage -n text proselint
%add_subpackage -n trig raptor2
%add_subpackage -n turtle raptor2
%add_subpackage -n vala vala
%add_subpackage -n verilog iverilog
%add_subpackage -n vim vim
%add_subpackage -n xhtml tidy
%add_subpackage -n xml /usr/bin/xmllint
%add_subpackage -n xslt /usr/bin/xmllint
%add_subpackage -n yacc byacc
%add_subpackage -n yaml yamllint perl-YAML-LibYAML
%add_subpackage -n yara yara
%add_subpackage -n z80 z80asm
%add_subpackage -n zsh zsh


# Intentional %%define here, intentionally after %%add_subpackage usage.
%define files_for_lang() \
%files %1 \
%license LICENCE \
%{vimfiles}/syntax_checkers/%1


%prep
%autosetup -n %upstream_name-%version -p1
# Use a free D compiler ldc
sed -i "s/dmd/ldc2/g" syntax_checkers/d/dmd.vim
# Use executable script from bindir
sed -i "s|expand\(.*sfile.*\).*|'%{_bindir}/erlang_check_file.erl'|" syntax_checkers/erlang/escript.vim

# Don't use /bin/env like shebangs.
grep -lr '#!.*/bin/env'  | while read file; do
    sed -i '1 s|#!.*/bin/env \(.*\)|#!/usr/bin/\1|' "$file"
done

rm -r syntax_checkers/actionscript
rm -r syntax_checkers/applescript
rm -r syntax_checkers/apiblueprint
rm -r syntax_checkers/bemhtml
rm -r syntax_checkers/bro
rm -r syntax_checkers/chef
# no cmakelint available in fedora
rm -r syntax_checkers/cmake
rm -r syntax_checkers/co
rm -r syntax_checkers/cobol
# coffee-script has been removed from fedora as of f39
rm -r syntax_checkers/coffee
rm -r syntax_checkers/cuda
# https://pagure.io/packaging-committee/issue/312
rm -r syntax_checkers/d
rm -r syntax_checkers/dart
# dockerfile-lint doesn't seem to be in Fedora yet:
# mock -r fedora-rawhide-x86_64 --install '/*/dockerfile*lint'
rm -r syntax_checkers/dockerfile
rm -r syntax_checkers/dustjs
rm -r syntax_checkers/handlebars
rm -r syntax_checkers/haxe
rm -r syntax_checkers/hss
rm -r syntax_checkers/jade
# rhbz#1912817
rm -r syntax_checkers/javascript
rm -r syntax_checkers/limbo
# https://pagure.io/packaging-committee/issue/312
rm -r syntax_checkers/lisp
rm -r syntax_checkers/markdown
rm -r syntax_checkers/mercury
rm -r syntax_checkers/nix
rm -r syntax_checkers/nroff
# mock -r fedora-rawhide-x86_64 --install '/*/pug*lint'
rm -r syntax_checkers/pug
rm -r syntax_checkers/r
rm -r syntax_checkers/racket
# mock -r fedora-rawhide-x86_64 --install '/*/lintr'
rm -r syntax_checkers/rmd
rm -r syntax_checkers/rnc
# rhbz#2311476
rm -r syntax_checkers/scala
rm -r syntax_checkers/slim
rm -r syntax_checkers/sml
# mock -r fedora-rawhide-x86_64 --install '/*/solc'
rm -r syntax_checkers/solidity
rm -r syntax_checkers/sql
rm -r syntax_checkers/stylus
# removed since nobody needs that, patches welcome!
rm -r syntax_checkers/svg
# Doesn't install binary:
# mock -r fedora-rawhide-x86_64 --install '/*/ttl'
rm -r syntax_checkers/turtle/ttl.vim
rm -r syntax_checkers/twig
rm -r syntax_checkers/typescript
# https://bugzilla.redhat.com/show_bug.cgi?id=1832470
rm -r syntax_checkers/vhdl
# dunno what to do with this
rm -r syntax_checkers/vue
# mock -r fedora-rawhide-x86_64 --install '/*/basex'
rm -r syntax_checkers/xquery
# mock -r fedora-rawhide-x86_64 --install '/*/pyang'
rm -r syntax_checkers/yang
rm -r syntax_checkers/zpt

%build

%install
mkdir -p %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{vimfiles}/autoload

cp      -rp       autoload/*                            %{buildroot}%{vimfiles}/autoload/
install -Dpm0644  doc/syntastic.txt                     %{buildroot}%{vimfiles}/doc/syntastic.txt
cp      -rp       plugin/                               %{buildroot}%{vimfiles}/plugin
cp      -rp       syntax_checkers/                      %{buildroot}%{vimfiles}/syntax_checkers

# not install -ped :
# applescript.vim    -> mac os
# coffe.vim          -> no coffe executable in repo
# cuda.vim           -> no nvcss executable in repo
# go.vim and go dir  -> no go executable in repo
# haskell.vim        -> no ghc-mod executable in repo
# haxe.vim           -> no haxe executable in repo
# less.vim           -> no lessc executable in repo
# matlab.vim         -> no mlint executable in repo
# z80.vim            -> no 80_syntax_checker.pyt executable in repo
# zpt.vim            -> no zptlint executable in repo

# Install AppData.
install -Dpm0644 %{SOURCE1} %{buildroot}%{appdata_dir}/vim-syntastic.metainfo.xml


%check
# Check the AppData add-on to comply with guidelines.
appstream-util validate-relax --nonet %{buildroot}%{appdata_dir}/vim-syntastic.metainfo.xml


%files
%license LICENCE
%doc _assets/screenshot_1.png README.markdown
%{vimfiles}/plugin/syntastic.vim
%{vimfiles}/plugin/syntastic
%{vimfiles}/doc/syntastic.txt
%dir %{vimfiles}/syntax_checkers/
%dir %{vimfiles}/autoload/syntastic/
%{vimfiles}/autoload/syntastic/log.vim
%{vimfiles}/autoload/syntastic/postprocess.vim
%{vimfiles}/autoload/syntastic/preprocess.vim
%{vimfiles}/autoload/syntastic//util.vim
%{appdata_dir}/vim-syntastic.metainfo.xml


%files_to_do


%changelog
* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 3.10.0-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Sep 12 2024 Martin Jackson <mhjacks@swbell.net> - 3.10.0-24
- scala has retired, so stop building it. bz#2311476

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.10.0-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.10.0-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.10.0-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Apr 7 2023 Martin Jackson <mhjacks@swbell.net> - 3.10.0-20
- cofee-script has retired, so stop building it. bz#2184502

* Thu Feb 23 2023 Martin Jackson <mhjacks@swbell.net> - 3.10.0-19
- Perl6 has come back! Thanks topazus.

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.10.0-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Jan 11 2023 Martin Jackson <mhjacks@swbell.net> - 3.10.0-17
- Remove perl6 dependencies for BZ#2159997. Rakudo etc have been retired for f38

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.10.0-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jul 08 2022 Jiri Vanek <jvanek@redhat.com> - 3.10.0-15
- Rebuilt for Drop i686 JDKs

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.10.0-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Oct 12 2021 Martin Jackson <mhjacks@swbell.net> - 3.10.0-13
- Change go dep to golang-bin from gcc-go. Obsolete earlier go subpackages

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.10.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jul  7 2021 Martin Jackson <mhjacks@swbell.net> - 3.10.0-11
- Obsolete rnc subpackage as well, and remove the rnc dir from package.
- Handle commented macro.

* Wed Jul  7 2021 Martin Jackson <mhjacks@swbell.net> - 3.10.0-10
- Stop building rnc subpackage due to rnv's retirement. (rhbz#1955850)

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.10.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jan 05 2021 Pavel Raiskup <praiskup@redhat.com> - 3.10.0-8
- drop javascript subpackage, javascript is going away from Fedora
  apparently
- this is probably the last update of vim-syntastic package, I plan to orphan it
  and start maintaining vim-ale instead:
  https://copr.fedorainfracloud.org/coprs/praiskup/vim-ale/

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.10.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 07 2020 Pavel Raiskup <praiskup@redhat.com> - 3.10.0-6
- switch the default YAML checker to yamllint (rhbz#1852240)

* Wed May 06 2020 Pavel Raiskup <praiskup@redhat.com> - 3.10.0-5
- disable vhdl subpackage

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.10.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Nov 20 2019 Markus Linnala <markus.linnala@gmail.com> - 3.10.0-3
- Add upstream patch vim-syntastic-3.10.0-5-rvim.patch to fix bz#1773723

* Wed Nov 20 2019 Markus Linnala <markus.linnala@gmail.com> - 3.10.0-2
- Simplify install/mkdir using install -D

* Thu Oct 03 2019 Pavel Raiskup <praiskup@redhat.com> - 3.10.0-1
- new upstream release (rhbz#1758038)

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.9.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Feb 12 2019 Pavel Raiskup <praiskup@redhat.com> - 3.9.0-4
- drop scriptlets, it is handled by vim-common's filetriggers
- use python3 shebangs (rhbz#1676190)

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.9.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.9.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Apr 23 2018 Pavel Raiskup <praiskup@redhat.com> - 3.9.0-1
- new upstream release, per release notes:
  https://github.com/vim-syntastic/syntastic/releases/tag/3.9.0

* Tue Apr 10 2018 Philippe Makowski <makowski@fedoraproject.org> - 3.8.0-12
- add text subpackage, fix rhbz#1562001

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.8.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.8.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Jul 14 2017 Petr Pisar <ppisar@redhat.com> - 3.8.0-9
- perl dependency renamed to perl-interpreter manually
  <https://fedoraproject.org/wiki/Changes/perl_Package_to_Install_Core_Modules>

* Fri Jul 14 2017 Pavel Raiskup <praiskup@redhat.com> - 3.8.0-8
- fix upgrade path for removed subpackages

* Thu Jul 13 2017 Petr Pisar <ppisar@redhat.com> - 3.8.0-7
- perl dependency renamed to perl-interpreter
  <https://fedoraproject.org/wiki/Changes/perl_Package_to_Install_Core_Modules>

* Thu Jul 13 2017 Pavel Raiskup <praiskup@redhat.com> - 3.8.0-6
- use python2 prefix for dependencies according to python package guidelines

* Wed Jun 28 2017 Pavel Raiskup <praiskup@redhat.com> - 3.8.0-5
- drop two subpackages which are not installable on aarch64/ppc64le due to
  missing dependencies, till we have fixed rel-eng scripts or we ratify
  https://pagure.io/packaging-committee/issue/312

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.8.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Nov 18 2016 Pavel Raiskup <praiskup@redhat.com> - 3.8.0-3
- drop ExclusiveArch hack for now, it doesn't work for sub-packages
  with rpm (rhbz#1394853) and pungi

* Wed Nov 16 2016 Pavel Raiskup <praiskup@redhat.com> - 3.8.0-2
- drop 'noarch' from ExclusiveArch

* Tue Nov 08 2016 Pavel Raiskup <praiskup@redhat.com> - 3.8.0-1
- new upstream release

* Mon Oct 31 2016 Kalev Lember <klember@redhat.com> - 3.7.0-9
- Use new ldc_arches macro

* Mon Oct 03 2016 Pavel Raiskup <praiskup@redhat.com> - 3.7.0-8
- use %%mono_arches

* Mon Oct 03 2016 Pavel Raiskup <praiskup@redhat.com> - 3.7.0-7
- Add ExclusiveArch tags appropriately, per discussion:
  https://lists.fedoraproject.org/archives/list/\
  devel@lists.fedoraproject.org/message/BFW6B2JX4RYUYVYL5LAFL34KVA2DXR47/

* Sun Sep 18 2016 Pavel Raiskup <praiskup@redhat.com> - 3.7.0-6
- don't use obsoletes < NVR

* Fri Sep 16 2016 Vít Ondruch <vondruch@redhat.com> - 3.7.0-5
- add AppData support

* Fri Sep 16 2016 Pavel Raiskup <praiskup@redhat.com> - 3.7.0-5
- rename to vim-syntastic

* Wed Sep 14 2016 Pavel Raiskup <praiskup@redhat.com> - 3.7.0-3
- add license to all subpackages
- condense the spec file a bit more
- remove cobol subpackage (open-cobol orphaned in F25+)

* Thu Sep 08 2016 Pavel Raiskup <praiskup@redhat.com> - 3.7.0-1
- unretirement, rebase to 3.7.0 (rhbz#1374138)

* Mon Sep 08 2014 Haïkel Guémar <hguemar@fedoraproject.org> - 3.5.0-1
- Upstream 3.5.0 (RHBZ #1074998, RHBZ #1135416)
- Fix BR to java-devel (RHBZ #1113308)
- Add R: syntastic-pod to syntastic-perl (RHBZ #1109519)
- Fix R: rubygem-sass for scss subpackage as scss is provided by rubygem-sass

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.4.0-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue May 20 2014 jonathan MERCIER <bioinfornatics@gmail.com> - 3.4.0-18
- Update to rev 3.4.0

* Mon Mar 10 2014 jonathan MERCIER <bioinfornatics@gmail.com> - 3.3.0-17.20140309gitda6520c
- Version 3.3.0

* Sun Mar 09 2014 jonathan MERCIER <bioinfornatics@gmail.com> - 2.3.0-16.20140309gitda6520c
- Update to latest rev

* Thu Oct 24 2013 Jonathan MERCIER <bioinfornatics@gmail.com> - 2.3.0-15.20131023gitd238665
- Update to rev d238665

* Sat Aug 10 2013 "Jonathan Mercier" <"Jonathan Mercier at gmail dot org"> - 2.3.0-14.20130809git48208d4
- Update to rev 48208d4

* Mon Aug 05 2013 "Jonathan Mercier" <"Jonathan Mercier at gmail dot org"> - 2.3.0-13.20130805gita4fa323
- Update to rev a4fa323

* Sun Aug 04 2013 "Jonathan Mercier" <"Jonathan Mercier at gmail dot org"> - 2.3.0-12.20130731gite380a86
- Update to rev e380a86

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3.0-11.20120917git72856e6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Jul 17 2013 Petr Pisar <ppisar@redhat.com> - 2.3.0-10.20120917git72856e6
- Perl 5.18 rebuild

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3.0-9.20120917git72856e6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Oct 03 2012 Jonathan MERCIER <bioinfornatics at gmail.com> - 2.3.0-8.20120917git72856e6
- fix spec

* Thu Sep 27 2012 Jonathan MERCIER <bioinfornatics at gmail.com> - 2.3.0-7.20120917git72856e6
- fix spec file

* Wed Sep 26 2012 Jonathan MERCIER <bioinfornatics at gmail.com> - 2.3.0-6.20120917git72856e6
- fix spec file

* Wed Sep 26 2012 Jonathan MERCIER <bioinfornatics at gmail.com> - 2.3.0-5.20120917git72856e6
- put  inautoload/syntastic/c.vimto c subpackage

* Mon Sep 17 2012 Jonathan MERCIER <bioinfornatics at gmail.com> - 2.3.0-4.20120917git72856e6
- Update to latest rev

* Thu Aug 23 2012 Jonathan MERCIER <bioinfornatics at gmail.com> - 2.3.0-3.20120802gite5dfcc3
- fix License
- remove unused macro
- Fix dependecies

* Mon Jun 18 2012  Jonathan MERCIER <bioinfornatics at gmail.com> - 2.3.0-2.20120617git1e94b98
- Update spec file

* Sun Jun 17 2012  Jonathan MERCIER <bioinfornatics at gmail.com> - 2.3.0-1.20120617git1e94b98
- initial release
