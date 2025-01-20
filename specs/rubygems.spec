# Upstream git:
# https://github.com/rubygems/rubygems.git
#

# Bundled libraries versions
%global molinillo_version 0.7.0
%global optparse_version 0.2.0
# TODO: Check the version if/when available in library.
%global tsort_version 0.1.0

# Requires versions
%global bundler_version 2.3.25
%global io_console_version 0.5.6
%global openssl_version 2.2.0
%global psych_version 3.3.0
%global rdoc_version 6.3.0

# The RubyGems library has to stay out of Ruby directory tree, since the
# RubyGems should be share by all Ruby implementations.
%global rubygems_dir %(ruby -e "puts RbConfig::CONFIG['rubygemsdir']")

# TODO: These folders should go into rubygem-filesystem but how to achieve it,
# since noarch package cannot provide arch dependent subpackages?
# http://rpm.org/ticket/78
%global gem_extdir %{_exec_prefix}/lib{,64}/gems

# Executing testsuite (enabling %%check section) will cause dependency loop.
# To avoid dependency loop when necessary, please set the following value to 0
%bcond_with bootstrap

# It cannot be relied on %%{_libdir} for noarch packages. Query Ruby for
# the right value.
# https://fedorahosted.org/rel-eng/ticket/5257
%{!?buildtime_libdir:%global buildtime_libdir $(ruby -rrbconfig -e 'puts RbConfig::CONFIG["libdir"]')}

Summary: The Ruby standard for packaging ruby libraries
Name: rubygems
Version: 3.3.25
Release: 206%{?dist}
# BSD-2-Clause: lib/rubygems/tsort/
# BSD-2-Clause OR RUBY: lib/rubygems/optparse/
# MIT: lib/rubygems/resolver/molinillo
License: (Ruby OR MIT) AND BSD-2-Clause AND (BSD-2-Clause OR RUBY) AND MIT

URL: https://rubygems.org/
Source0: https://rubygems.org/rubygems/%{name}-%{version}.tgz
# Sources from the works by Vít Ondruch <vondruch@redhat.com>
# NOTE: Keep Source1 in sync with ruby.spec.
Source1: operating_system.rb
# http://seclists.org/oss-sec/2013/q3/att-576/check_CVE-2013-4287_rb.bin
# Slightly modified for exit status
Source11: check_CVE-2013-4287.rb
# http://seclists.org/oss-sec/2013/q3/att-621/check_CVE-2013-XXXX_rb.bin
# Slightly modified for exit status,
# Also modified to match:
# http://seclists.org/oss-sec/2013/q3/605
Source12: check_CVE-2013-4363.rb
# Fix ruby_version abuse.
# https://bugs.ruby-lang.org/issues/11002
# NOTE: Keep this patch in sync with ruby.spec.
Patch0: ruby-2.3.0-ruby_version.patch
# Bundler installation does not respec `--destdir`. But we ship Bundler in
# independent package, therefore just ignore the installation altogether.
# https://github.com/rubygems/rubygems/issues/3604
Patch1: rubygems-3.1.3-Avoid-Bundler-installation.patch


Requires:   ruby(release)
Recommends: rubygem(bundler) >= %{bundler_version}
Recommends: rubygem(rdoc) >= %{rdoc_version}
Recommends: rubygem(io-console) >= %{io_console_version}
Requires:   rubygem(openssl) >= %{openssl_version}
Requires:   rubygem(psych) >= %{psych_version}
BuildRequires: ruby(release)
BuildRequires: rubygems-devel
%if %{without bootstrap}
# For mkmf.rb
BuildRequires: ruby-devel
BuildRequires: rubygem(test-unit)
BuildRequires: %{_bindir}/cmake
BuildRequires: %{_bindir}/git
BuildRequires: %{_bindir}/gcc
BuildRequires: rubygem(rake)
BuildRequires: rubygem(webrick)
%endif
Provides:   gem = %{version}-%{release}
Provides:   ruby(rubygems) = %{version}-%{release}
# https://github.com/rubygems/rubygems/pull/1189#issuecomment-121600910
Provides:   bundled(rubygem-molinillo) = %{molinillo_version}
BuildArch:  noarch

%description
RubyGems is the Ruby standard for publishing and managing third party
libraries.

%package    doc
Summary:    Documentation for %{name}
License:    Ruby or MIT
Requires:   ruby(%{name}) = %{version}-%{release}
BuildArch:  noarch

%description doc
Documentation for %{name}.

%prep
%setup -q

%patch 0 -p1
%patch 1 -p1

%build
# Nothing

%install
mkdir -p %{buildroot}{%{rubygems_dir},%{gem_dir}}/
GEM_HOME=%{buildroot}%{gem_dir} \
    ruby setup.rb \
    --document rdoc,ri \
    --prefix=/ \
    --backtrace \
    --no-regenerate-binstubs \
    --destdir=%{buildroot}%{rubygems_dir}/

mkdir -p %{buildroot}%{_bindir}
mv %{buildroot}%{rubygems_dir}/bin/gem %{buildroot}%{_bindir}/.
rm -rf %{buildroot}%{rubygems_dir}/bin

mv %{buildroot}/%{rubygems_dir}/lib/* %{buildroot}%{rubygems_dir}/.
# No longer needed
rmdir %{buildroot}%{rubygems_dir}/lib

# Kill bundled certificates, as they should be part of ca-certificates.
for cert in \
  .document \
  rubygems.org/GlobalSignRootCA.pem \
  rubygems.org/GlobalSignRootCA_R3.pem
do
  rm %{buildroot}%{rubygems_dir}/rubygems/ssl_certs/$cert
  rm -d $(dirname %{buildroot}%{rubygems_dir}/rubygems/ssl_certs/$cert) || :
done
# Ensure there is not forgotten any certificate.
test ! "$(ls -A %{buildroot}%{rubygems_dir}/rubygems/ssl_certs/ 2>/dev/null)"

# Install custom operating_system.rb.
mkdir -p %{buildroot}%{rubygems_dir}/rubygems/defaults
install -cpm 0644 %{SOURCE1} %{buildroot}%{rubygems_dir}/rubygems/defaults/

# Create gem folders.
mkdir -p %{buildroot}%{gem_dir}/{cache,gems,specifications,extensions,doc,plugins}
mkdir -p %{buildroot}%{gem_extdir}/ruby

# Create below
mkdir -p %{buildroot}%{gem_dir}/specifications/default

# Remove bundled bundler
rm -vr %{buildroot}%{rubygems_dir}/bundler*


%check
# Create an empty operating_system.rb, so that the system's one doesn't get used,
# otherwise the test suite fails.
mkdir -p lib/rubygems/defaults
touch lib/rubygems/defaults/operating_system.rb

# Check Bundler version.
[ "`RUBYOPT=-Ibundler/lib ruby -rbundler/version -e 'puts Bundler::VERSION'| tail -1`" \
  == '%{bundler_version}' ]

# Check Molinillo version correctness.
[ "`RUBYOPT=-Ilib ruby -e 'module Gem; class Resolver; end; end; require %{rubygems/resolver/molinillo/lib/molinillo/gem_metadata}; puts Gem::Resolver::Molinillo::VERSION' | tail -1`" \
  == '%{molinillo_version}' ]

# Check optparse version correctness.
[ "`RUBYOPT=-Ilib ruby -e 'require %{rubygems/optparse/lib/optparse}; puts Gem::OptionParser::Version' | tail -1`" \
  == '%{optparse_version}' ]

%if %{without bootstrap}
# util directory with changelog generator are not shipped in release archive.
mv test/test_changelog_generator.rb{,.disabled}

# Put all required libraries on the `$LOAD_PATH`, where the original Ruby
# `require` can find them. This prevents the RubyGems load machinery from
# running and failing to find `gem.build_complete` files for sytem packages
# and therefore raising warnings such as: "Ignoring json-2.5.1 because its
# extensions are not built. Try: gem pristine json --version 2.5.1".
# https://github.com/rubygems/rubygems/pull/4446
export RUBYOPT="-I$(ruby -e 'size = $LOAD_PATH.size; %w(rake test-unit rdoc webrick).each {|r| require r}; puts $LOAD_PATH[...-size].join ?:')"

# Rakefile is not shipped anymore => emulate its content.
# https://github.com/rubygems/rubygems/blob/v3.3.22/Rakefile#L56-L64
# The `test_realworld_{default_gem,upgraded_default_gem}` needs the same
# treatment as the have in Ruby repository. Use `GEM_COMMAND` to skip them.
GEM_COMMAND="skip test_realworld_{default_gem,upgraded_default_gem}" \
  ruby -Itest:bundler/lib:lib -e 'Dir.glob "./test/**/test_*.rb", &method(:require)' - \

# CVE vulnerability check
ruby %{SOURCE11}
ruby %{SOURCE12}
%endif

%files
%doc CODE_OF_CONDUCT.md
%doc CHANGELOG.md
%doc CONTRIBUTING.md
%doc MAINTAINERS.txt
%doc POLICIES.md
%doc README.md
%doc UPGRADING.md
%license MIT.txt LICENSE.txt
%{_bindir}/gem
%dir %{rubygems_dir}
%{rubygems_dir}/rubygems
%{rubygems_dir}/rubygems.rb
%exclude %{rubygems_dir}/rubygems/optparse/.*
%license %{rubygems_dir}/rubygems/optparse/COPYING
%license %{rubygems_dir}/rubygems/resolver/molinillo/LICENSE
%exclude %{rubygems_dir}/rubygems/tsort/.*
%license %{rubygems_dir}/rubygems/tsort/LICENSE.txt

# Explicitly include only RubyGems directory strucure to avoid accidentally
# packaged content.
%dir %{gem_dir}
%dir %{gem_dir}/build_info
%dir %{gem_dir}/cache
%dir %{gem_dir}/doc
%dir %{gem_dir}/extensions
%dir %{gem_dir}/gems
%dir %{gem_dir}/plugins
%dir %{gem_dir}/specifications
%dir %{gem_dir}/specifications/default
%dir %{_exec_prefix}/lib*/gems
%dir %{_exec_prefix}/lib*/gems/ruby

%files	doc
%doc %{gem_dir}/doc/*


%changelog
* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.25-206
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.25-205
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.25-204
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.25-203
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.25-202
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Nov 03 2022 Jun Aruga <jaruga@redhat.com> - 3.3.25-201
- Update to RubyGems 3.3.25.
  Resolves: rhbz#2132563

* Thu Sep 08 2022 Vít Ondruch <vondruch@redhat.com> - 3.3.22-201
- Update to RubyGems 3.3.22.
  Resolves: rhbz#1941091
  Resolves: rhbz#2046966

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.14-204
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.14-203
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.14-202
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Thu Mar 11 2021 Vít Ondruch <vondruch@redhat.com> - 3.2.14-201
- Enable additional test cases with Ruby load path setup correctly.

* Fri Mar 05 2021 Vít Ondruch <vondruch@redhat.com> - 3.2.14-200
- Update to RubyGems 3.2.14.
  Resolves: rhbz#1905813
  Resolves: rhbz#1923699

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.4-202
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.4-201
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jun 24 2020 Vít Ondruch <vondruch@redhat.com> - 3.1.4-200
- Update to RubyGems 3.1.4.

* Thu May 28 2020 Vít Ondruch <vondruch@redhat.com> - 3.1.3-201
- Fix `require` behavior allowing to load libraries multiple times.
  Resolves: rhbz#1835836

* Thu May 07 2020 Vít Ondruch <vondruch@redhat.com> - 3.1.3-200
- Update to RubyGems 3.1.3.

* Thu May 07 2020 Pavel Valena <pvalena@redhat.com> - 3.0.3-106
- Upgrade to Rubygems 3.0.3.

* Thu May 07 2020 Vít Ondruch <vondruch@redhat.com> - 2.6.13-106
- Fix FTBFS due to Ruby 2.7, OpenSSL 1.1.1 and CMake 2.8+ incompatibilities.
  Resolves: rhbz#1800046
- Drop rubygems-devel subpackage.

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.13-105
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.13-104
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.13-103
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.13-102
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.13-101
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Sep 05 2017 Vít Ondruch <vondruch@redhat.com> - 2.6.13-100
- Update to RubyGems 2.6.13.

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.10-101
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Mar 07 2017 Vít Ondruch <vondruch@redhat.com> - 2.6.10-100
- Update to RubyGems 2.6.10.

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.8-102
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.8-101
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jul 10 2015 Vít Ondruch <vondruch@redhat.com> - 2.4.8-100
- Update to RubyGems 2.4.8.

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org>
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org>
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed May 07 2014 Vít Ondruch <vondruch@redhat.com> - 2.2.2-100
- Update to RubyGems 2.2.2.

* Fri Jan 10 2014 Mamoru TASAKA <mtasaka@fedoraproject.org> - 2.1.11-115
- Add extension directory also to WhichCommand::gem_paths (bug 1051169)

* Fri Dec 13 2013 Mamoru TASAKA <mtasaka@fedoraproject.org> - 2.1.11-114
- Add extension directory to contains_requirable_file (bug 1041391)

* Thu Nov 14 2013 Mamoru TASAKA <mtasaka@fedoraproject.org> - 2.1.11-113
- Update to 2.1.11

* Sat Oct 26 2013 Mamoru TASAKA <mtasaka@fedoraproject.org> - 2.1.10-112
- Update to 2.1.10

* Mon Oct 21 2013 Mamoru TASAKA <mtasaka@fedoraproject.org> - 2.1.9-111
- Update to 2.1.9

* Tue Oct 15 2013 Mamoru TASAKA <mtasaka@fedoraproject.org> - 2.0.12-110
- Backport from 2.1.x branch to fix concurrent requires issue
  (ref:bug 989574)

* Tue Oct 15 2013 Mamoru TASAKA <mtasaka@fedoraproject.org> - 2.0.12-109
- Update to 2.0.12
- Un-unlink %%{_sysconfdir}/pki/tls/cert.pem with discussion with
  Vít Ondruch <vondruch@redhat.com>

* Wed Oct  9 2013 Mamoru TASAKA <mtasaka@fedoraproject.org> - 2.0.11-108
- Add BR: cmake for TestGemExtCmakeBuilder

* Wed Oct  9 2013 Mamoru TASAKA <mtasaka@fedoraproject.org> - 2.0.11-107
- Update to 2.0.11

* Wed Sep 25 2013 Mamoru TASAKA <mtasaka@fedoraproject.org> - 2.0.10-106
- Update to 2.0.10 (fix for CVE-2013-4363 included)

* Mon Sep 23 2013 Mamoru TASAKA <mtasaka@fedoraproject.org> - 2.0.9-105
- Update to 2.0.9
- Fix %%gem_dir/doc ownership (bug 1008866)
- Patch for CVE-2013-4363

* Tue Sep 10 2013 Mamoru TASAKA <mtasaka@fedoraproject.org> - 2.0.8-104
- Update to 2.0.8, which fixes CVE-2013-4287

* Fri Aug 16 2013 Mamoru TASAKA <mtasaka@fedoraproject.org> - 2.0.7-103
- Update to 2.0.7

* Thu Aug 15 2013 Mamoru TASAKA <mtasaka@fedoraproject.org> - 2.0.6-102
- Update to 2.0.6

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.5-101
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Mon Jul 15 2013 Mamoru TASAKA <mtasaka@fedoraproject.org> - 2.0.5-100
- Update to 2.0.5
- Show backtrace when %%gem_install fails

* Thu Jul 04 2013 Vít Ondruch <vondruch@redhat.com> - 2.0.3-2
- Fix RubyGems search paths when building gems with native extension
  (rhbz#979133).

* Thu Mar 21 2013 Mamoru TASAKA <mtasaka@fedoraproject.org> - 2.0.3-1
- Update to 2.0.3

* Fri Mar 08 2013 Mamoru TASAKA <mtasaka@fedoraproject.org> - 2.0.0-108
- Don't mark rpm config file as %%config (fpc#259)

* Tue Mar 05 2013 Vít Ondruch <vondruch@redhat.com> - 2.0.0-107
- Avoid "method redefined;" warnings due to modified operating_system.rb.

* Tue Mar  5 2013 Mamoru Tasaka <mtasaka@fedoraproject.org> - 2.0.0-106
- Fix regex for creating native extension directory
  (Vít Ondruch <vondruch@redhat.com>)

* Sun Mar  3 2013 Mamoru TASAKA <mtasaka@fedoraproject.org> - 2.0.0-105
- Kill creating unneeded LOCAL_LIBS\ = directory under
  %%gem_libdir when building native extension

* Wed Feb 27 2013 Mamoru TASAKA <mtasaka@fedoraproject.org> - 2.0.0-104
- Kill %%gem_extdir

* Tue Feb 26 2013 Vít Ondruch <vondruch@redhat.com> - 2.0.0-103
- Prevent squash of %%gem_install with following line.

* Mon Feb 25 2013 Mamoru TASAKA <mtasaka@fedoraproject.org> - 2.0.0-102
- Provide %%gem_extdir_mri

* Mon Feb 25 2013 Mamoru TASAKA <mtasaka@fedoraproject.org> - 2.0.0-101
- Split out ri-generated documentation

* Mon Feb 25 2013 Mamoru TASAKA <mtasaka@fedoraproject.org> - 2.0.0-100
- Update to 2.0.0

* Mon Feb 25 2013 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1.8.25-3
- Backport %%gem_install macro

* Tue Feb  5 2013 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1.8.25-2
- Fix rubygem(json) path

* Tue Feb  5 2013 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1.8.25-1
- 1.8.25

* Tue Feb  5 2013 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1.8.24-4
- Bump release

* Wed Sep 05 2012 Vít Ondruch <vondruch@redhat.com> - 1.8.24-3
- Fixed Fedora 18 mass rebuild issue.

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.8.24-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Apr 28 2012 Mamoru Tasaka <mtasaka@fedoraproject.org> - 1.8.24-1
- 1.8.24

* Sat Apr 21 2012 Mamoru Tasaka <mtasaka@fedoraproject.org> - 1.8.23-20
- 1.8.23
- Use system-wide cert.pem

* Wed Apr 18 2012 Mamoru Tasaka <mtasaka@fedoraproject.org> - 1.8.22-1
- 1.8.22

* Thu Jan 26 2012 Vít Ondruch <vondruch@redhat.com> - 1.8.15-2
- Make test suite green.

* Thu Jan 26 2012 Mamoru Tasaka <mtasaka@fedoraproject.org> - 1.8.15-1
- 1.8.15

* Thu Jan 26 2012 Mamoru Tasaka <mtasaka@fedoraproject.org> - 1.8.11-10
- Incorpolate works by Vít Ondruch <vondruch@redhat.com>
  made for ruby 1.9.x

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.8.11-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Nov 22 2011 Mamoru Tasaka <mtasaka@fedoraproject.org> - 1.8.11-1
- 1.8.11

* Sun Aug 28 2011 Mamoru Tasaka <mtasaka@fedoraproject.org> - 1.8.10-1
- 1.8.10

* Thu Aug 25 2011 Mamoru Tasaka <mtasaka@fedoraproject.org> - 1.8.9-1
- 1.8.9

* Sun Aug 21 2011 Mamoru Tasaka <mtasaka@fedoraproject.org> - 1.8.8-1
- 1.8.8

* Sat Aug  6 2011 Mamoru Tasaka <mtasaka@fedoraproject.org> - 1.8.7-1
- 1.8.7

* Wed Jul 27 2011 Mamoru Tasaka <mtasaka@fedoraproject.org> - 1.8.6-1
- 1.8.6

* Sat Jun 25 2011 Mamoru Tasaka <mtasaka@fedoraproject.org> - 1.8.5-2
- Fix Gem.latest_load_paths (for rubygem-gettext FTBFS)
- Fix Gem.all_load_paths (for rubygem-gettext FTBFS, although it is already
  deprecated from 1.7.0)

* Wed Jun  1 2011 Mamoru Tasaka <mtasaka@fedoraproject.org> - 1.8.5-1
- Try 1.8.5

* Tue May 24 2011 Mamoru Tasaka <mtasaka@fedoraproject.org> - 1.7.2-2
- Handle gemspec file with containing "invalid" date format
  generated with psych (ref: bug 706914)

* Sat Apr 30 2011 Mamoru Tasaka <mtasaka@fedoraproject.org> - 1.7.2-1
- Update to 1.7.2

* Sat Mar 12 2011 Mamoru Tasaka <mtasaka@fedoraproject.org> - 1.6.2-1
- Update to 1.6.2

* Fri Mar  4 2011 Mamoru Tasaka <mtasaka@fedoraproject.org> - 1.6.1-1
- Update to 1.6.1
- Patch2, 4 upstreamed

* Thu Mar  3 2011 Mamoru Tasaka <mtasaka@fedoraproject.org> - 1.6.0-1
- Update to 1.6.0

* Sun Feb 27 2011 Mamoru Tasaka <mtasaka@fedoraproject.org> - 1.5.3-1
- Update to 1.5.3

* Sun Feb 20 2011 Mamoru Tasaka <mtasaka@fedorapeople.org> - 1.5.2-1
- Update to 1.5.2
- Show rdoc process verbosely in verbose mode

* Fri Feb 11 2011 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 1.5.0-2
- Modify in-sync patch to keep the original behavior (for testsuite)
- Patch to make testsuite succeed, enabling testsuite

* Thu Feb 10 2011 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 1.5.0-1
- Update to 1.5.0

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Oct  8 2010 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 1.3.7-2
- Show build process of extension library in sync

* Mon May 17 2010 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 1.3.7-1
- Update to 1.3.7, dropping upstreamed patch

* Wed Apr 28 2010 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 1.3.6-1
- Update to 1.3.6
- Show prefix with gem contents by default as shown in --help

* Mon Sep 21 2009 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 1.3.5-1
- Update to 1.3.5

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sun Nov 09 2008 Jeroen van Meeuwen <kanarip@kanarip.com> - 1.3.1-1
- New upstream version

* Tue Sep 16 2008 David Lutterkort <dlutter@redhat.com> - 1.2.0-2
- Bump release because I forgot to check in newer patch

* Tue Sep 16 2008 David Lutterkort <dlutter@redhat.com> - 1.2.0-1
- Updated for new setup.rb
- Simplified by removing conditionals that were needed for EL-4;
  there's just no way we can support that with newer rubygems

* Wed Sep  3 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 0.9.4-2
- fix license tag

* Fri Jul 27 2007 David Lutterkort <dlutter@redhat.com> - 0.9.4-1
- Conditionalize so it builds on RHEL4

* Tue Feb 27 2007 David Lutterkort <dlutter@redhat.com> - 0.9.2-1
- New version
- Add patch0 to fix multilib sensitivity of Gem::dir (bz 227400)

* Thu Jan 18 2007 David Lutterkort <dlutter@redhat.com> - 0.9.1-1
- New version; include LICENSE.txt and GPL.txt
- avoid '..' in gem_dir to work around a bug in gem installer
- add ruby-rdoc to requirements

* Tue Jan  2 2007 David Lutterkort <dlutter@redhat.com> - 0.9.0-2
- Fix gem_dir to be arch independent
- Mention dual licensing in License field

* Fri Dec 22 2006 David Lutterkort <dlutter@redhat.com> - 0.9.0-1
- Updated to 0.9.0
- Changed to agree with Fedora Extras guidelines

* Mon Jan  9 2006 David Lutterkort <dlutter@redhat.com> - 0.8.11-1
- Updated for 0.8.11

* Sun Oct 10 2004 Omar Kilani <omar@tinysofa.org> 0.8.1-1ts
- First version of the package
