Name:		perl-MCE-Shared
Version:	1.893
Release:	2%{?dist}
Summary:	MCE extension for sharing data, supporting threads and processes
License:	GPL-1.0-or-later OR Artistic-1.0-Perl
URL:		https://metacpan.org/release/MCE-Shared
Source0:	https://cpan.metacpan.org/authors/id/M/MA/MARIOROY/MCE-Shared-%{version}.tar.gz
BuildArch:	noarch
# Module Build
BuildRequires:	coreutils
BuildRequires:	findutils
BuildRequires:	make
BuildRequires:	perl-generators
BuildRequires:	perl-interpreter
BuildRequires:	perl(ExtUtils::MakeMaker)
# Module Runtime
BuildRequires:	perl(base)
BuildRequires:	perl(bytes)
BuildRequires:	perl(Carp)
BuildRequires:	perl(constant)
BuildRequires:	perl(Errno)
BuildRequires:	perl(if)
BuildRequires:	perl(IO::Handle)
BuildRequires:	perl(MCE) >= 1.889
BuildRequires:	perl(MCE::Mutex)
BuildRequires:	perl(MCE::Signal)
BuildRequires:	perl(MCE::Util)
BuildRequires:	perl(overload)
BuildRequires:	perl(overloading)
BuildRequires:	perl(POSIX)
BuildRequires:	perl(Scalar::Util)
BuildRequires:	perl(Socket)
BuildRequires:	perl(Storable) >= 2.04
BuildRequires:	perl(strict)
BuildRequires:	perl(Time::HiRes)
BuildRequires:	perl(warnings)
# Optional Functionality
# Note: MCE will pull in Sereal if it is available
BuildRequires:	perl(IO::FDPass) >= 1.2
# Test Suite
BuildRequires:	perl(MCE::Flow)
BuildRequires:	perl(open)
BuildRequires:	perl(Test::More) >= 0.88
BuildRequires:	perl(utf8)
# Dependencies
Requires:	perl(IO::FDPass) >= 1.2
Requires:	perl(MCE) >= 1.889
Requires:	perl(overloading)
Requires:	perl(POSIX)
Requires:	perl(Storable) >= 2.04

# Remove bogus dependency on perl(PDL)
%global __requires_exclude ^perl\\(PDL\\)

%description
This module provides data sharing capabilities for MCE, supporting threads and
processes. MCE::Hobo provides threads-like parallelization for running code
asynchronously.

%prep
%setup -q -n MCE-Shared-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
make pure_install DESTDIR=%{buildroot}
find %{buildroot} -type f -name .packlist -delete
%{_fixperms} -c %{buildroot}

%check
make test

%files
%license LICENSE Copying
%doc Changes README.md
%{perl_vendorlib}/MCE/
%{_mandir}/man3/MCE::Hobo.3*
%{_mandir}/man3/MCE::Shared.3*
%{_mandir}/man3/MCE::Shared::Array.3*
%{_mandir}/man3/MCE::Shared::Base.3*
%{_mandir}/man3/MCE::Shared::Cache.3*
%{_mandir}/man3/MCE::Shared::Common.3*
%{_mandir}/man3/MCE::Shared::Condvar.3*
%{_mandir}/man3/MCE::Shared::Handle.3*
%{_mandir}/man3/MCE::Shared::Hash.3*
%{_mandir}/man3/MCE::Shared::Minidb.3*
%{_mandir}/man3/MCE::Shared::Ordhash.3*
%{_mandir}/man3/MCE::Shared::Queue.3*
%{_mandir}/man3/MCE::Shared::Scalar.3*
%{_mandir}/man3/MCE::Shared::Sequence.3*
%{_mandir}/man3/MCE::Shared::Server.3*

%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.893-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Tue Sep 10 2024 Paul Howarth <paul@city-fan.org> - 1.893-1
- Update to 1.893 (rhbz#2311118)
  - Improve MCE::Hobo exiting when signaled

* Thu Aug 22 2024 Paul Howarth <paul@city-fan.org> - 1.892-1
- Update to 1.892
  - Fix for MCE::Hobo, Can't call method "len" on an undefined value during
    global destruction

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.891-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jun 20 2024 Paul Howarth <paul@city-fan.org> - 1.891-1
- Update to 1.891
  - In scalar context, MCE::Hobo->init returns a guard to call finish
    automatically upon leaving the { scope } (i.e. omitting finish)

* Tue Jun 11 2024 Paul Howarth <paul@city-fan.org> - 1.890-1
- Update to 1.890
  - Revert back to calling CORE::rand() to set the internal seed; MCE::Hobo
    cannot assume the srand or setter function used by the application for
    predictability
    - https://perlmonks.org/?node_id=11159834
    - https://perlmonks.org/?node_id=11159827
  - Add class method MCE::Hobo->seed to retrieve the seed

* Mon Jun 10 2024 Paul Howarth <paul@city-fan.org> - 1.889-1
- Update to 1.889
  - Improve support for PDL

* Thu Jun  6 2024 Paul Howarth <paul@city-fan.org> - 1.888-1
- Update to 1.888
  - Apply workaround for PDL::srand in MCE::Hobo
    (https://www.perlmonks.org/?node_id=11159773)
  - Add PDL::srand (v2.062~v2.089) and PDL::srandom (v2.089_01+)

* Sun May 26 2024 Paul Howarth <paul@city-fan.org> - 1.887-1
- Update to 1.887
  - Improve reaping of completed workers in MCE::Hobo

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.886-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.886-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Sep 14 2023 Paul Howarth <paul@city-fan.org> - 1.886-1
- Update to 1.886
  - Add Android support; this required moving MCE::Shared::Base::Common out of
    MCE::Shared::Base to separate file MCE::Shared::Common
  - Bump MCE dependency to 1.889

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.885-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jun  9 2023 Paul Howarth <paul@city-fan.org> - 1.885-1
- Update to 1.885
  - Fix typo in Queue dequeue_timed documentation

* Thu Jun  8 2023 Paul Howarth <paul@city-fan.org> - 1.884-1
- Update to 1.884
  - Add missing return statement(s) in Condvar and Queue
  - Move tests for condvar timedwait to xt/condvar_timedwait.t

* Wed Jun  7 2023 Paul Howarth <paul@city-fan.org> - 1.883-1
- Update to 1.883
  - Bump MCE dependency to 1.886
  - Added dequeue_timed method to MCE::Shared::Queue
  - Fixed taint mode in MCE::Shared::Sequence _sprintf
  - Remove unused Queue vars in MCE::Shared::Server, since 1.867

* Wed May 31 2023 Paul Howarth <paul@city-fan.org> - 1.881-1
- Update to 1.881
  - Bump MCE dependency to 1.885
  - Improved reliability on the Windows platform

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.880-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Jan  4 2023 Paul Howarth <paul@city-fan.org> - 1.880-1
- Update to 1.880
  - Bump MCE dependency to 1.883
  - Improved 05_mce_hobo.t test

* Sat Dec  3 2022 Paul Howarth <paul@city-fan.org> - 1.879-1
- Update to 1.879
  - Update the error status if MCE::Hobo died due to receiving a signal
  - Improved the timeout handler in MCE::Hobo and MCE::Shared::Condvar
  - Fixed private functions _quit and _trap not setting the return value

* Mon Oct 10 2022 Paul Howarth <paul@city-fan.org> - 1.878-1
- Update to 1.878
  - Improved reliability on the Windows platform
  - Added deeply-shared demonstration to POD
- Use SPDX-format license tag

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.877-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jun 01 2022 Jitka Plesnikova <jplesnik@redhat.com> - 1.877-2
- Perl 5.36 rebuild

* Tue May 24 2022 Paul Howarth <paul@city-fan.org> - 1.877-1
- Update to 1.877
  - Replace http with https in documentation and meta files
  - Call PDL::set_autopthread_targ(1); disables PDL auto-threading
  - Allow sharing additional PDL objects via class methods: pdl_sbyte,
    pdl_ulong, pdl_ulonglong, pdl_ldouble, pdl_grandom, and pdl_zero

* Sun Feb 20 2022 Paul Howarth <paul@city-fan.org> - 1.876-1
- Update to 1.876
  - Improved suppressing the PDL CLONE warning; piddles should not be naively
    copied into new threads

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.875-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Dec  3 2021 Paul Howarth <paul@city-fan.org> - 1.875-1
- Update to 1.875
  - Resolved edge case with _fill_index in MCE::Shared::Ordhash
  - Updated STORE, DELETE, and internal _fill_index
  - Added tests to t/07_shared_ordhash.t

* Fri Dec  3 2021 Paul Howarth <paul@city-fan.org> - 1.874-1
- Update to 1.874
  - Bumped MCE dependency to 1.874
  - MCE::Hobo update
    - Improved _ordhash
    - Renamed JOINED to REAPED in code for better clarity
    - Specify a percentage for max_workers
    - Added t/05_mce_hobo_max_workers.t

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.873-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri May 21 2021 Jitka Plesnikova <jplesnik@redhat.com> - 1.873-3
- Perl 5.34 rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.873-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sun Aug  2 2020 Paul Howarth <paul@city-fan.org> - 1.873-1
- Update to 1.873
  - Resolved construction MCE::Shared->share hanging when specifying a module
    that does not exist

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.872-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jun 23 2020 Jitka Plesnikova <jplesnik@redhat.com> - 1.872-2
- Perl 5.32 rebuild

* Mon Jun 15 2020 Paul Howarth <paul@city-fan.org> - 1.872-1
- Update to 1.872
  - Added open to required dependencies
  - Set default encodings on standard filehandles in tests using UTF-8
  - Added setnx method to MCE::Shared::{ Cache, Hash and Ordhash }
  - Added hsetnx method to MCE::Shared::Minidb
  - Updated keys, pairs, and values in
    MCE::Shared::{ Array, Cache, Hash and Ordhash }
  - The MCE::Shared project is feature complete

* Wed May 13 2020 Paul Howarth <paul@city-fan.org> - 1.871-1
- Update to 1.871
  - Switched test for skipping unicode testing for MCE::Shared::Cache from
    needing Perl > 5.10.1 to needing Scalar::Util ≥ 1.22

* Tue May 12 2020 Paul Howarth <paul@city-fan.org> - 1.869-1
- Update to 1.869
  - Disabled unicode testing for MCE::Shared::Cache on Perl 5.10.1; testing
    for keys containing unicode is failing on RedHat 6.x but passing in
    meta::cpan (smoke tests)
  - Share array and hash deeply: only when using the TIE interface; this
    resolves an edge case for the OO interface and passing nested items during
    construction
  - Bumped MCE dependency to 1.868

* Mon May 11 2020 Paul Howarth <paul@city-fan.org> - 1.868-1
- Update to 1.868
  - Bug fix for UTF-8 issues during inter-process communication
    - This update required undoing optimizations specific to scalar args
    - Essentially, IPC involves serialization for everything going forward
    - Install Sereal::Encoder and Sereal::Decoder for better performance
  - Improved MCE::Hobo with threads-like detach capability (see POD)
  - Resolved MCE::Hobo stalling MCE::Shared::Server during global clean-up
  - Improved IPC in MCE::Shared::Queue with permanent fast-like dequeue
    including dequeue_nb; going forward, the fast and barrier options are
    silently ignored if specified (i.e. no-op)
  - Improved IPC performance on Linux
  - Completed threads-like detach capability in MCE::Hobo

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.864-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Dec  4 2019 Paul Howarth <paul@city-fan.org> - 1.864-1
- Update to 1.864
  - Use monotonic clock if available in MCE::Hobo->yield
    (see https://www.perlmonks.org/?node_id=11109673)
  - Bumped MCE dependency to 1.864

* Mon Nov 25 2019 Paul Howarth <paul@city-fan.org> - 1.863-1
- Update to 1.863
  - Use MCE::Channel for MCE::Hobo->yield not to incur unnecessary delays due
    to busy shared-manager process
  - Re-factored recent changes regarding IPC safety in MCE::Shared::Server;
    this update defers signal handling for HUP, INT, PIPE, QUIT, TERM, and
    custom handlers during IPC without incurring a performance penalty (see
    POD section labled "DEFER SIGNAL" in MCE::Signal 1.863)
  - Reverted $hobo->exit back to sending the SIGQUIT signal in MCE::Hobo now
    that MCE::Shared::Server defers signal during IPC
  - Improved reliability for spawning MCE::Hobo inside threads including nested
    parallelization, made possible using a global lock $MCE::_GMUTEX in MCE
    1.863
  - Updated signal handling in mce-examples/framebuffer on GitHub
  - Bumped MCE dependency to 1.863

* Thu Sep 19 2019 Paul Howarth <paul@city-fan.org> - 1.862-1
- Update to 1.862
  - The edge cases regarding signal handling have finally been resolved for
    MCE::Hobo; see mce-examples/framebuffer on GitHub
  - Bumped MCE dependency to 1.862

* Mon Sep 16 2019 Paul Howarth <paul@city-fan.org> - 1.860-1
- Update to 1.860
  - Signal-handling update release
  - SIGINT and SIGTERM safety for shared objects during IPC
  - IPC safety in MCE::Hobo during SIGINT and SIGTERM
  - Method $hobo->exit in MCE::Hobo now sends the SIGINT signal for extra
    reliability with MCE::Shared (previously SIGQUIT)
  - Bumped MCE dependency to 1.860

* Mon Sep  9 2019 Paul Howarth <paul@city-fan.org> - 1.850-1
- Update to 1.850
  - More safety around clean-up code in MCE::Shared::Server
  - Bumped MCE dependency to 1.850

* Mon Sep  9 2019 Paul Howarth <paul@city-fan.org> - 1.849-1
- Update to 1.849
  - Fixed edge case in MCE::Hobo when reaping inside a signal handler
  - Guard clean-up code in MCE::Shared::Server during global destruction
  - Configured extra data channel used for reaping Hobos and exporting
  - Optimized reaping in MCE::Hobo when void_context is set
  - Added list_pids class method to MCE::Hobo
  - Added pid class method to MCE::Shared
  - Bumped MCE dependency to 1.849

* Wed Sep  4 2019 Paul Howarth <paul@city-fan.org> - 1.848-1
- Update to 1.848
  - Fixed broken examples in the MCE::Shared documentation
  - Bumped MCE dependency to 1.848

* Tue Sep  3 2019 Paul Howarth <paul@city-fan.org> - 1.847-1
- Update to 1.847
  - Obsolete RedHat MCE-Shared-1.841-Sereal-deps.patch file; this patch file is
    no longer needed and finally resolved with this release
  - Updated PDL examples in the documentation including Cookbook on GitHub:
    - Resolved segmentation fault in global cleanup for shared PDL objects
    - Added missing pdl_random class method to MCE::Shared
  - Bumped MCE dependency to 1.847

* Tue Aug 27 2019 Paul Howarth <paul@city-fan.org> - 1.846-1
- Update to 1.846
  - Fixed code tags in documentation
  - Bumped MCE dependency to 1.846

* Mon Aug 26 2019 Paul Howarth <paul@city-fan.org> - 1.845-1
- Update to 1.845
  - Improved is_joinable, is_running, list_joinable, and list_running in
    MCE::Hobo
  - Added parallel Graphics::Framebuffer demonstrations:
    https://github.com/marioroy/mce-examples/tree/master/framebuffer
  - Bumped MCE dependency to 1.845

* Thu Aug 15 2019 Paul Howarth <paul@city-fan.org> - 1.844-1
- Update to 1.844
  - Completed validation running Kelp and Raisin apps with MCE::Shared
    - For example, constructing shared objects at the top of the script (i.e.
      MCE::Shared->scalar, MCE::Shared->cache, et cetera)
    - Shared objects are accessible by Plack workers (i.e. Starman)
  - Disable internal signal handling for the shared-manager process if
    spawned from inside a thread or process
  - MCE::Hobo workers exit immediately upon receiving a SIGSEGV signal; this
    safegaurds IPC from stalling inside the manager process
  - Enhanced the _wait_one private function in MCE::Hobo
  - Removed Prima from the list for auto-enabling the posix_exit option; Prima
    (since 1.52) is parallel safe during global cleanup
  - Reached 100%% Pod coverage

* Wed Jul 24 2019 Paul Howarth <paul@city-fan.org> - 1.843-1
- Update to 1.843
  - Updated results in MCE::Hobo (Parallel::ForkManager-like demonstration)
  - Bumped MCE dependency to 1.843

* Mon Jul 22 2019 Paul Howarth <paul@city-fan.org> - 1.842-1
- Update to 1.842
  - The Windows hack introduced in 1.841 is 2x slower for one edge case, so
    reverted the Windows hack in MCE::Shared::Server
  - Fixed race condition abnormalities in MCE::Hobo
  - Added Parallel::ForkManager-like demonstration to MCE::Hobo
  - Bumped MCE dependency to 1.842

* Sun Jul  7 2019 Paul Howarth <paul@city-fan.org> - 1.841-1
- Update to 1.841
  - IPC update; raising reliability across multiple platforms
  - Improved the hack for the Windows platform in MCE::Shared::Server
  - Support reading a shared <DATA> handle residing in the main script without
    involving the IO::FDPass module
  - Added barrier option to MCE::Shared::Queue allowing one to disable
  - Added mutex locking for all shared objects, previously just condvars
  - Added void_context option to MCE::Hobo
  - Renamed POD method headers from '=item' to '=head2' in Shared classes
  - Bumped MCE dependency to 1.839
  - Removed MANIFEST.SKIP

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 1.840-3
- Perl 5.30 rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.840-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jan  4 2019 Paul Howarth <paul@city-fan.org> - 1.840-1
- Update to 1.840
  - Improved destroy and exit cleanup in MCE::Shared::Server

* Tue Aug 28 2018 Paul Howarth <paul@city-fan.org> - 1.839-1
- Update to 1.839
  - Seeds the Math::Random::MT::Auto generator automatically when present in
    MCE::Hobo, similarly to Math::Random and Math::Prime::Util, to avoid child
    processes sharing the same seed value as the parent and each other; the new
    seed is computed using the current seed
  - Updated MCE::Shared::Cache to support optional argument "expires_in" for
    set and sugar methods
  - Updated MCE::Shared documentation
  - Bumped MCE dependency to 1.837

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.838-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Jun 29 2018 Jitka Plesnikova <jplesnik@redhat.com> - 1.838-2
- Perl 5.28 rebuild

* Tue Jun 26 2018 Paul Howarth <paul@city-fan.org> - 1.838-1
- Update to 1.838
  - Fixed deeply-shared regressions
    See https://perlmonks.pairsite.com/?node_id=1216790
  - Applied small optimizations
  - Bumped MCE dependency to 1.836

* Wed Mar 14 2018 Paul Howarth <paul@city-fan.org> - 1.836-1
- Update to 1.836
  - Added chameneos demonstration to MCE::Shared::Condvar
  - Load IO::Handle for extra stability, preventing workers loading uniquely
  - Load Net::HTTP and Net::HTTPS before spawning if present LWP::UserAgent
    See http://www.perlmonks.org/?node_id=1199760
    and http://www.perlmonks.org/?node_id=1199891
  - Bumped MCE dependency to 1.835

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.835-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Jan 23 2018 Paul Howarth <paul@city-fan.org> - 1.835-1
- Update to 1.835
  - Added max_workers method to MCE::Hobo
  - Improved Queue await and dequeue performance on the Windows platform
  - Added chameneos-redux parallel demonstrations on GitHub:
    https://github.com/marioroy/mce-examples/tree/master/chameneos
  - Bumped MCE dependency to 1.834

* Mon Dec 18 2017 Paul Howarth <paul@city-fan.org> - 1.834-1
- Update to 1.834
  - Fixed croak handling inside MCE::Shared::Server
  - Enhanced sequence (bounds_only) to return optional 3rd value (id)
  - Improved seconds method for _delay package inside MCE::Hobo
  - Improved clear and get methods for shared objects
  - Tweaked shared_cache_lru test script

* Wed Nov 22 2017 Paul Howarth <paul@city-fan.org> - 1.833-1
- Update to 1.833
  - Condvar timedwait supports floating seconds via Time::HiRes; the
    documentation was correct, but not high resolution in code
  - Added LWP::UserAgent to list for enabling posix_exit
  - Improved number-sequence generation for big integers
  - Improved exiting (CLOSE, DESTROY) during cleanup state
  - Improved signal handling when server is waiting on IO
  - Updated "OBJECT SHARING" section in documentation
  - Bumped MCE dependency to 1.832

* Mon Oct  9 2017 Paul Howarth <paul@city-fan.org> - 1.832-1
- Update to 1.832
  - Added STFL (Terminal UI) to list for enabling posix_exit
    (see http://www.perlmonks.org/?node_id=1200923)
  - Math::Prime::Util random numbers now unique between Hobo workers
    (see http://www.perlmonks.org/?node_id=1200960)
  - Bumped MCE dependency to 1.831

* Wed Sep 20 2017 Paul Howarth <paul@city-fan.org> - 1.831-1
- Update to 1.831
  - Resolved crash on the Windows platform for older Perl (< v5.18); older Perl
    must continue to run the shared-server as a thread
  - Re-enabled Condvar testing on the Windows platform
- Rebase Sereal-deps patch

* Mon Sep 18 2017 Paul Howarth <paul@city-fan.org> - 1.830-1
- Update to 1.830
  - Disabled Condvar tests on Windows

* Fri Sep 15 2017 Paul Howarth <paul@city-fan.org> - 1.829-1
- Update to 1.829
  - Disabled Condvar tests on Windows machine without IO::FDPass

* Wed Sep 13 2017 Paul Howarth <paul@city-fan.org> - 1.828-1
- Update to 1.828
  Bug Fixes
  - Fixed bug in MCE::Shared::Queue
  Enhancements
  - Refactored MCE::Hobo, MCE::Shared and MCE::Shared::Server
  - Preserved lexical type for numbers during IPC
  - Added Coro and Win32::GUI to list for enabling posix_exit
  - Added encoder and decoder methods for overriding serialization
  - Added parallel HTTP get demonstration using AnyEvent to MCE::Hobo
  - Added Inline::Python, Logger, and Tie::File demonstrations to MCE::Shared
  - Added DBM-Sharing section to the POD documentation
  - Added iterator method to MCE::Cache
  - Improved auto-dereferencing for shared arrays, hashes, and scalars
  - Improved open method for non-shared file-handles in MCE::Shared::Handle.
  - Improved shared-PDL support; updated MCE::Cookbook on GitHub
  - Improved signal handling, including nested parallel-sessions
  - Improved running MCE::Hobo and MCE::Shared with PDL
  - Improved taint mode via perl -T
  - In MCE::Hobo, waitall and waitone are now aliases to wait_all and wait_one
    respectively for backwards compatibility
  - No longer loads threads on the Windows platform in MCE::Shared::Server;
    this enables MCE::Hobo to spin faster, including lesser memory consumption
  - Removed extra white-space from POD documentation
  - Validated MCE::Hobo and MCE::Shared on SmartOS
  - Bumped MCE dependency to 1.830
- Rebase Sereal-deps patch

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.826-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Jun 05 2017 Jitka Plesnikova <jplesnik@redhat.com> - 1.826-2
- Perl 5.26 rebuild

* Wed May  3 2017 Paul Howarth <paul@city-fan.org> - 1.826-1
- Update to 1.826
  - Reduced memory consumption
  - Clarified "limitations" section in MCE::Share::{ Condvar, Handle, Queue }
  - Clarified "extra functionality" section in MCE::Shared
  - Bumped MCE dependency to 1.829

* Sat Apr 29 2017 Paul Howarth <paul@city-fan.org> - 1.825-1
- Update to 1.825
  - Do not enable barrier mode for Queue on the Windows platform
  - Fixed MCE::Hobo on the Windows platform for older Perl < v5.16
  - Added Curses and Prima to list for enabling the posix_exit option
  - Added module option for using a class implicitly when tie'ing a variable
  - Added unbless option when exporting a shared object
  - Improved support for running MCE::Hobo on the NetBSD platform
  - Enhanced IPC and signal handling, reduced memory consumption
  - Bumped MCE dependency to 1.828

* Fri Apr  7 2017 Paul Howarth <paul@city-fan.org> - 1.824-1
- Update to 1.824
  - Fixed bug introduced in 1.818, syswrite data to a shared file handle

* Wed Apr  5 2017 Paul Howarth <paul@city-fan.org> - 1.823-1
- Update to 1.823
  - Do not enable barrier mode in Queue if constructed inside a thread or for
    the fast => 1 option
  - Fixed leaked handles during destruction: MCE::Shared::{ Condvar, Queue }
  - Updated MCE::Shared not to croak when running Perl in taint mode via
    perl -T; failing -T were MCE::Shared::{ Handle, Sequence, Server }
  - Bumped MCE dependency to 1.827

* Mon Apr  3 2017 Paul Howarth <paul@city-fan.org> - 1.822-1
- Update to 1.822
  - Performance improvements in MCE::Shared::Queue
  - When IO::FDPass is missing, croak with error if constructing a Condvar
    or Queue and the shared-manager process has not been started manually
  - Is now safe running MCE::Hobo with the Wx GUI toolkit (wxWidgets)
  - Bumped MCE dependency to 1.826

* Sat Apr  1 2017 Paul Howarth <paul@city-fan.org> - 1.820-1
- Update to 1.820
  - Check for EINTR during sysread and syswrite
  - Improved non-shared handles constructed with MCE::Shared::Handle
  - Reap MCE::Hobo's from script exiting during development process
  - Calibrated the number of data-channels for IPC
  - Completed validation for using MCE::Shared with 200+ cores
  - Completed validation for running MCE on a box having 100+ cores
  - Tuned the number of data-channels for IPC, similar to MCE
  - Bumped MCE dependency to 1.824

* Sun Mar 19 2017 Paul Howarth <paul@city-fan.org> - 1.817-1
- Update to 1.817
  - Fixed broken SIG{'PIPE'} handling: e.g. script.pl | head
  - Improved reliability when running MCE::Shared with threads
  - Added parallel Net::Pcap and Ping demonstrations on GitHub:
    https://github.com/marioroy/mce-examples/tree/master/network
  - Default to ':raw' for BINMODE in MCE::Shared::Handle
  - Optimized 'dequeue' method in MCE::Shared::Queue
  - Refactored MCE::Hobo to spawn children on the Windows platform
  - Bumped MCE dependency to 1.821
- Update Sereal dependency patch

* Mon Mar  6 2017 Paul Howarth <paul@city-fan.org> - 1.816-1
- Update to 1.816
  - Optimized SHIFT and UNSHIFT methods in MCE::Shared::Ordhash

* Sat Mar  4 2017 Paul Howarth <paul@city-fan.org> - 1.815-1
- Update to 1.815
  - Fixed issue with localizing AUTOFLUSH variable before autoflush handles
  - Bumped MCE dependency to 1.819

* Thu Mar  2 2017 Paul Howarth <paul@city-fan.org> - 1.814-1
- Update to 1.814
  - Fixed an issue in regards to deeply sharing an array or hash
  - Replaced Sereal with Sereal::Decoder and Sereal::Encoder in Makefile,
    inside recommends section; ditto for META files
  - Revised limitations section in documentation, in regards to not having
    IO::FDPass, e.g. Condvar, Handle, and Queue
  - Added 'end' method to MCE::Shared::Queue
  - Updated documentation on dequeue and pending
  - Bumped MCE dependency to 1.818

* Thu Feb 23 2017 Paul Howarth <paul@city-fan.org> - 1.813-1
- Update to 1.813
  - Revised the main description in MCE::Shared::Cache
  - Improved write performance by up to 8 percent
  - Fixed spelling mistakes
  - Revised the description of posix_exit in MCE::Hobo

* Mon Feb 20 2017 Paul Howarth <paul@city-fan.org> - 1.812-1
- Update to 1.812
  - Improved performance for MCE::Shared::Cache; this is now a hybrid LRU-plain
    cache implementation
  - Added parallel demonstration at the end of the documentation
  - Bumped MCE dependency to 1.814 for the example to run
  - Tweaked MCE::Shared::Ordhash and MCE::Shared::Server

* Thu Feb 16 2017 Paul Howarth <paul@city-fan.org> - 1.811-1
- Update to 1.811
  - Bumped IO::FDPass minimum version to 1.2 if not already installed (1.1+)
    and have a CC compiler on hand; IO::FDPass is optional otherwise
  - Support csh redirection in Makefile.PL via bash for locating C compiler

* Wed Feb 15 2017 Paul Howarth <paul@city-fan.org> - 1.810-1
- Update to 1.810
  - Bumped minimum requirement for Sereal to 3.015 when available; added check
    ensuring matching version for Encoder and Decoder
- Add patch to avoid unintentional hard dependencies on Sereal

* Tue Feb 14 2017 Paul Howarth <paul@city-fan.org> - 1.809-1
- Update to 1.809
  - Fixed bug in MCE::Shared::Queue (dequeue_nb) when queue has zero items
  - Applied small optimization in MCE::Shared::Sequence
  - Added MCE::Shared::Cache, a fast and memory-efficient LRU-cache module
  - Added pipeline methods to MCE::Shared::Array, Hash, Minidb, and Ordhash
  - Added recommends section to Makefile and META files: IO::FDPass, Sereal
  - Added cross-platform template to MCE::Hobo for making an executable
  - Added hobo_timeout option to MCE::Hobo for timeout capability
    Also, imply posix_exit => 1 when Gearman::XS is present
  - Added MCE::Hobo + Gearman demonstrations (xs and non-xs) on GitHub:
    https://github.com/marioroy/mce-examples/tree/master/gearman_xs
    https://github.com/marioroy/mce-examples/tree/master/gearman
  - Changed kilobytes and megabytes to kibiBytes (KiB) and mebiBytes (MiB)
    respectively inside the documentation
  - Having IO::FDPass is beneficial for Condvar(s), Handle(s), and Queue(s);
    thus, append IO::FDPass to PREREQ_PM if we can and not already installed
    (run MCE_PREREQ_EXCLUDE_IO_FDPASS=1 perl Makefile.PL to bypass the check)
  - Improved documentation for QUERY STRING in various helper classes
  - Updated SYNOPSIS in various helper classes
  - Updated LOCKING section in MCE::Shared

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.808-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sat Dec 10 2016 Paul Howarth <paul@city-fan.org> - 1.808-1
- Update to 1.808
  - Optimized the barrier synchronization example in MCE::Shared::Condvar

* Thu Nov 24 2016 Paul Howarth <paul@city-fan.org> - 1.807-1
- Update to 1.807
  - Refactored MCE::Hobo
  - Improved reliability on the Windows platform by using threads
  - Bug fixes for test scripts

* Wed Nov  2 2016 Paul Howarth <paul@city-fan.org> - 1.806-1
- Update to 1.806
  - Added a new section titled LOCKING to the MCE::Shared documentation
  - Tweaked shared-manager-loop delay - applies to MSWin32 only

* Tue Oct  4 2016 Paul Howarth <paul@city-fan.org> - 1.805-3
- Incorporate package review feedback (#1378028)
  - Add dependencies on perl(overloading), perl(Storable) ≥ 2.04 and
    perl(Symbol), missed by perl-generators

* Fri Sep 23 2016 Paul Howarth <paul@city-fan.org> - 1.805-1
- Update to 1.805
  - Fixed close method in shared-handle to work with Perl5i; support for
    Perl5i is on Unix only - do not use threads
  - Bumped MCE dependency to 1.805

* Wed Sep 21 2016 Paul Howarth <paul@city-fan.org> - 1.804-2
- Sanitize for Fedora submission

* Fri Sep 16 2016 Paul Howarth <paul@city-fan.org> - 1.804-1
- Initial RPM build
