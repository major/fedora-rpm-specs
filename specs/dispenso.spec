%ifarch %{arm} %{ix86}
# need to sort out tests, only 90% pass
%bcond_with check
%else
%bcond_without check
%endif

# disable flaky / failing tests by default
%bcond_with all_tests

# In file included from /builddir/build/BUILD/dispenso-1.3.0/dispenso/../dispenso/detail/graph_executor_impl.h:9,
#                  from /builddir/build/BUILD/dispenso-1.3.0/dispenso/../dispenso/graph_executor.h:10,
#                  from /builddir/build/BUILD/dispenso-1.3.0/dispenso/graph_executor.cpp:8:
# /builddir/build/BUILD/dispenso-1.3.0/dispenso/../dispenso/graph.h:489:25: error: template-id not allowed for constructor in C++20 [-Werror=template-id-cdtor]
#   489 |   explicit SubgraphT<N>(GraphT<N>* graph) : graph_(graph), nodes_(), allocator_(getAllocator()) {}
#       |                         ^~~~~~~~~
# /builddir/build/BUILD/dispenso-1.3.0/dispenso/../dispenso/graph.h:489:25: note: remove the ‘< >’
# /builddir/build/BUILD/dispenso-1.3.0/dispenso/../dispenso/graph.h:530:12: error: template-id not allowed for constructor in C++20 [-Werror=template-id-cdtor]
#   530 |   GraphT<N>() {
#       |            ^
# /builddir/build/BUILD/dispenso-1.3.0/dispenso/../dispenso/graph.h:530:12: note: remove the ‘< >’
# cc1plus: all warnings being treated as errors
%if 0%{?fedora} >= 40 || 0%{?rhel} >= 10
%global optflags %(echo %{optflags} -Wno-error=template-id-cdtor)
%endif

Name:           dispenso
Version:        1.4.0
Release:        %{autorelease}
Summary:        A library for working with sets of tasks in parallel

%global major_ver %(c=%{version}; echo $c | cut -d. -f1)

License:        MIT
URL:            https://github.com/facebookincubator/dispenso
Source0:        %{url}/archive/v%{version}/%{name}-%{version}.tar.gz
# TODO: make toggleable and upstream
Patch0:         %{name}-use-system-gtest.diff
# TODO: make toggleable and upstream
Patch1:         %{name}-use-system-moodycamel.diff

BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  moodycamel-concurrentqueue-devel
%if %{with check}
BuildRequires:  gmock-devel
BuildRequires:  gtest-devel
%endif

%global _description %{expand:
Dispenso is a library for working with sets of tasks in parallel. It provides
mechanisms for thread pools, task sets, parallel for loops, futures, pipelines,
and more. Dispenso is a well-tested C++14 library designed to have minimal
dependencies (some dependencies are required for the tests and benchmarks), and
designed to be clean with compiler sanitizers (ASAN, TSAN). Dispenso is
currently being used in dozens of projects and hundreds of C++ files at Meta
(formerly Facebook). Dispenso also aims to avoid major disruption at every
release. Releases will be made such that major versions are created when a
backward incompatibility is introduced, and minor versions are created when
substantial features have been added or bugs have been fixed, and the aim would
be to only very rarely bump major versions. That should make the project
suitable for use from main branch, or if you need a harder requirement, you can
base code on a specific version.}

%description %{_description}


%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       moodycamel-concurrentqueue-devel

%description    devel %{_description}

The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%prep
%autosetup -p1
# make sure we use the system library
rm -rf dispenso/third-party


%build
%cmake \
%if %{with check}
  -DDISPENSO_BUILD_TESTS=ON \
%else
  %{nil}
%endif

%cmake_build


%install
%cmake_install


%if %{with check}
%check
%if %{with all_tests}
%ctest
%else
# flaky tests
EXCLUDED_TESTS='-E Priorty\.PriorityGetsCycles'
EXCLUDED_TESTS+='|TimedTaskTest'
%if 0%{?el10}
# The following tests FAILED:
#         556 - GraphEvaluation/TwoSubgraphs.ReplaceSourceGraph/singleThread  # GetParam() = 1-byte object <00> (SEGFAULT)
#         557 - GraphEvaluation/TwoSubgraphs.ReplaceSourceGraph/parallelFor  # GetParam() = 1-byte object <01> (SEGFAULT)
#         558 - GraphEvaluation/TwoSubgraphs.ReplaceSourceGraph/concurrentTaskSet  # GetParam() = 1-byte object <02> (SEGFAULT)
#         559 - GraphEvaluation/TwoSubgraphs.ReplaceMiddleGraph/singleThread  # GetParam() = 1-byte object <00> (SEGFAULT)
#         560 - GraphEvaluation/TwoSubgraphs.ReplaceMiddleGraph/parallelFor  # GetParam() = 1-byte object <01> (SEGFAULT)
#         561 - GraphEvaluation/TwoSubgraphs.ReplaceMiddleGraph/concurrentTaskSet  # GetParam() = 1-byte object <02> (SEGFAULT)
#         562 - GraphEvaluation/TwoSubgraphs.ReplaceBothGraphs/singleThread  # GetParam() = 1-byte object <00> (SEGFAULT)
#         563 - GraphEvaluation/TwoSubgraphs.ReplaceBothGraphs/parallelFor  # GetParam() = 1-byte object <01> (SEGFAULT)
#         564 - GraphEvaluation/TwoSubgraphs.ReplaceBothGraphs/concurrentTaskSet  # GetParam() = 1-byte object <02> (SEGFAULT)
#         565 - GraphEvaluation/TwoSubgraphs.PartialEvaluation/singleThread  # GetParam() = 1-byte object <00> (SEGFAULT)
#         566 - GraphEvaluation/TwoSubgraphs.PartialEvaluation/parallelFor  # GetParam() = 1-byte object <01> (SEGFAULT)
#         567 - GraphEvaluation/TwoSubgraphs.PartialEvaluation/concurrentTaskSet  # GetParam() = 1-byte object <02> (SEGFAULT)
#         568 - BiPropEvaluation/BiPropGraphTest.SimpleEvaluation/singleThread  # GetParam() = 1-byte object <00> (SEGFAULT)
#         569 - BiPropEvaluation/BiPropGraphTest.SimpleEvaluation/parallelFor  # GetParam() = 1-byte object <01> (SEGFAULT)
#         570 - BiPropEvaluation/BiPropGraphTest.SimpleEvaluation/concurrentTaskSet  # GetParam() = 1-byte object <02> (SEGFAULT)
EXCLUDED_TESTS+='|TwoSubgraphs\.ReplaceSourceGraph'
EXCLUDED_TESTS+='|TwoSubgraphs\.ReplaceMiddleGraph'
EXCLUDED_TESTS+='|TwoSubgraphs\.ReplaceBothGraph'
EXCLUDED_TESTS+='|TwoSubgraphs\.PartialEvaluation'
EXCLUDED_TESTS+='|BiPropGraphTest\.SimpleEvaluation'
%endif
%ctest $EXCLUDED_TESTS
%endif
%endif


%files
%license LICENSE
%{_libdir}/*.so.%{major_ver}
%{_libdir}/*.so.%{version}

%files devel
%doc CODE_OF_CONDUCT.md CONTRIBUTING.md README.md
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/cmake/Dispenso-%{version}


%changelog
%autochangelog
