%define ver 1.49.0
%define file_version 1_49_0
%define short_version 1_49

#Define to 0 to not generate the pdf documentation
%define build_pdf 0
%define package_pdf 0


%define disable_long_double 0

%define boost_libs1 libboost_date_time libboost_filesystem%{lib_appendix} libboost_graph%{lib_appendix}
%define boost_libs2 libboost_iostreams libboost_math%{lib_appendix} libboost_test%{lib_appendix}
%define boost_libs3 libboost_program_options libboost_python%{lib_appendix} libboost_serialization%{lib_appendix}
%define boost_libs4 libboost_signals libboost_system%{lib_appendix} libboost_thread%{lib_appendix}
%define boost_libs5 libboost_wave libboost_regex%{lib_appendix} libboost_regex%{lib_appendix}
%define boost_libs6 libboost_random libboost_chrono%{lib_appendix} libboost_locale%{lib_appendix}
%define boost_libs7 libboost_timer

%define all_libs %boost_libs0 %boost_libs2 %boost_libs3 %boost_libs4 %boost_libs5 %boost_libs6 %boost_libs7


%define debug_package_requires %{all_libs}

Name:           boost
BuildRequires:  boost-jam
BuildRequires:  dos2unix
BuildRequires:  chrpath
BuildRequires:  gcc-c++
BuildRequires:  bzip2-devel
BuildRequires:  zlib-devel
BuildRequires:  expat-devel
BuildRequires:  libicu-devel
BuildRequires:  python-devel
BuildRequires:  xz
BuildRequires:  fdupes
Url:            http://www.boost.org
Summary:        Boost C++ Libraries
License:        BSD-3-Clause
Group:          Development/Libraries/C and C++
Version:        1.49.0
Release:        0
Source0:        %{name}_%{file_version}.tar.bz2
Source1:        boost-rpmlintrc
Source4:        existing_extra_docs

%define _docdir %{_datadir}/doc/packages/boost

%description
Boost provides free peer-reviewed portable C++ source libraries. The
emphasis is on libraries that work well with the C++ Standard Library.
One goal is to establish "existing practice" and provide reference
implementations so that the Boost libraries are suitable for eventual
standardization. Some of the libraries have already been proposed for
inclusion in the C++ Standards Committee's upcoming C++ Standard
Library Technical Report.

Although Boost was begun by members of the C++ Standards Committee
Library Working Group, membership has expanded to include nearly two
thousand members of the C++ community at large.

This package is mainly needed for updating from a prior version, the
dynamic libraries are found in their respective package. For development
using Boost, you also need the boost-devel package. For documentation,
see the boost-doc package.



%package        devel
Summary:        Development package for Boost C++
Group:          Development/Libraries/C and C++
Requires:       %{all_libs}
Requires:       libstdc++-devel

%description    devel
This package contains all that is needed to develop/compile
applications that use the Boost C++ libraries. For documentation see
the documentation packages (html, man or pdf).



%package     -n boost-license
Summary:        Boost License
Group:          Development/Libraries/C and C++
BuildArch:      noarch

%description    -n boost-license
This package contains the license boost is provided under.


%package        -n libboost_date_time
Summary:        Boost::Date.Time Runtime libraries
Group:          System/Libraries
Requires:       boost-license
Provides:       boost-datetime

%description -n libboost_date_time
This package contains the Boost Date.Time runtime libraries.


%package     -n libboost_filesystem
Summary:        Boost::Filesystem Runtime Libraries
Group:          System/Localization
Requires:       boost-license
Provides:       boost-filesystem

%description    -n libboost_filesystem
This package contains the Boost::Filesystem libraries.


%package        -n libboost_graph
Summary:        Boost::Graph Runtime Libraries
Group:          System/Libraries
Requires:       boost-license
Provides:       boost-graph

%description    -n libboost_graph
This package contains the Boost::Graph Runtime libraries.


%package        -n libboost_iostreams
Summary:        Boost::IOStreams Runtime Libraries
Group:          System/Libraries
Requires:       boost-license
Provides:       boost-iostreams

%description    -n libboost_iostreams
This package contains the Boost::IOStreams Runtime libraries.


%package        -n libboost_math
Summary:        Boost::Math Runtime Libraries
Group:          System/Libraries
Requires:       boost-license
Provides:       boost-math

%description    -n libboost_math
This package contains the Boost::Math Runtime libraries.



%package        -n libboost_test
Summary:        Boost::Test Runtime Libraries
Group:          System/Libraries
Requires:       boost-license
Provides:       boost-test

%description    -n libboost_test
This package contains the Boost::Test runtime libraries.


%package        -n libboost_program_options
Summary:        Boost::ProgramOptions Runtime libraries
Group:          System/Libraries
Requires:       boost-license
Provides:       boost-program-options

%description    -n libboost_program_options
This package contains the Boost::ProgramOptions Runtime libraries.


%package        -n libboost_python
Summary:        Boost::Python Runtime Libraries
Group:          System/Libraries
Requires:       boost-license
Provides:       boost-python

%description    -n libboost_python
This package contains the Boost::Python Runtime libraries.


%package        -n libboost_serialization
Summary:        Boost::Serialization Runtime Libraries
Group:          System/Libraries
Requires:       boost-license
Provides:       boost-serialization

%description    -n libboost_serialization
This package contains the Boost::Serialization Runtime libraries.


%package        -n libboost_signals
Summary:        Boost::Signals Runtime Libraries
Group:          System/Libraries
Requires:       boost-license

%description    -n libboost_signals
This package contains the Boost::Signals Runtime libraries.


%package        -n libboost_system
Summary:        Boost::System Runtime Libraries
Group:          System/Libraries
Requires:       boost-license
Provides:       boost-system

%description    -n libboost_system
This package contains the Boost::System runtime libraries.


%package        -n libboost_thread
Summary:        Boost::Thread Runtime Libraries
Group:          System/Libraries
Requires:       boost-license
Provides:       boost-thread

%description    -n libboost_thread
This package contains the Boost::Thread runtime libraries.


%package        -n libboost_wave
Summary:        Boost::Wave Runtime Libraries
Group:          System/Libraries
Requires:       boost-license
Provides:       boost-wave

%description    -n libboost_wave
This package contains the Boost::Wave runtime libraries.


%package        -n libboost_regex
Summary:        The Boost::Regex runtime library
Group:          System/Libraries
Requires:       boost-license
Provides:       boost-regex

%description    -n libboost_regex
This package contains the Boost::Regex runtime library.

%package        -n libboost_random
Summary:        The Boost::Random runtime library
Group:          System/Libraries
Requires:       boost-license
Provides:       boost-random

%description    -n libboost_random
This package contains the Boost::Random runtime library.

%package        -n libboost_chrono
Summary:        The Boost::Chrono runtime library
Group:          System/Libraries
Requires:       boost-license
Provides:       boost-chrono

%description    -n libboost_chrono
This package contains the Boost::Chrono runtime library.

%package        -n libboost_locale
Summary:        The Boost::Locale runtime library
Group:          System/Libraries
Requires:       boost-license
Provides:       boost-locale

%description    -n libboost_locale
This package contains the Boost::Locale runtime library.

%package        -n libboost_timer
Summary:        The Boost::Timer runtime library
Group:          System/Libraries
Requires:       boost-license
Provides:       boost-timer

%description    -n libboost_timer
This package contains the Boost::Timer runtime library.


%prep
%setup -q -n %{name}_%{file_version} 
#everything in the tarball has the executable flag set ...
find -type f ! \( -name \*.sh -o -name \*.py -o -name \*.pl \) -exec chmod -x {} +

#stupid build machinery copies .orig files
find . -name \*.orig -exec rm {} +

%build
find . -type f -exec chmod u+w {} +

# Now build it
J_P=%{jobs}
J_G=$(getconf _NPROCESSORS_ONLN)
[ $J_G -gt 64 ] && J_G=64

if test -z "$JOBS"; then
  JOBS=$J_G
else
  test 1 -gt "$JOBS" && JOBS=1
fi
if test "$JOBS" == "0"; then
  JOBS=1
fi

# In case you want more parallel jobs then autobuild grants you
#if [ $J_P -gt $J_I ]; then
#  JOBS=$J_G
#fi
%if %{disable_long_double}
export LONG_DOUBLE_FLAGS="--disable-long-double"
%endif
BJAM_CONFIG="-d2 -j$JOBS -sICU_PATH=%{_prefix}"
PYTHON_VERSION=$(python -c 'import sys; print sys.version[:3]')
PYTHON_FLAGS="--with-python-root=/usr --with-python-version=$PYTHON_VERSION"
REGEX_FLAGS="--with-icu"
export EXPAT_INCLUDE=/usr/include EXPAT_LIBPATH=%{_libdir} REGEX_FLAGS="--with-icu"
export PYTHON_FLAGS

cat << EOF >user-config.jam
# Boost.Build Configuration

# Compiler configuration
using gcc ;

# Python configuration
using python : ${PYTHON_VERSION} : %{_prefix} ;
EOF


%if %build_mpi
cat << EOF >>user-config.jam
using mpi ;
EOF

# Set PATH, MANPATH and LD_LIBRARY_PATH
source /var/mpi-selector/data/$(rpm --qf "%{NAME}-%{VERSION}" -q openmpi).sh
%endif

sh ./bootstrap.sh
./b2


%install
# Now build it
J_P=%{jobs}
J_G=$(getconf _NPROCESSORS_ONLN)
[ $J_G -gt 64 ] && J_G=64

if test -z "$JOBS"; then
  JOBS=$J_G
else
  test 1 -gt "$JOBS" && JOBS=1
fi
if test "$JOBS" == "0"; then
  JOBS=1
fi

# In case you want more parallel jobs then autobuild grants you
if [ $J_P -gt $J_G ]; then
  JOBS=$J_G
fi

BJAM_CONFIG="-d2 -j$JOBS -sICU_PATH=%{_prefix}"
PYTHON_VERSION=$(python -c 'import sys; print sys.version[:3]')
PYTHON_FLAGS="--with-python-root=/usr --with-python-version=$PYTHON_VERSION"
REGEX_FLAGS="--with-icu"
export EXPAT_INCLUDE=/usr/include EXPAT_LIBPATH=%{_libdir} REGEX_FLAGS="--with-icu"
export PYTHON_FLAGS

# Set PATH, MANPATH and LD_LIBRARY_PATH
%if %build_mpi
source /var/mpi-selector/data/$(rpm --qf "%{NAME}-%{VERSION}" -q openmpi).sh
%endif

%{_bindir}/bjam ${BJAM_CONFIG} ${LONG_DOUBLE_FLAGS} --user-config=user-config.jam \
	--prefix=%{buildroot}%{_prefix} \
	--exec-prefix=$%{buildroot}%{_prefix} \
	--libdir=%{buildroot}%{_libdir} \
	--includedir=%{buildroot}%{_includedir} \
	install || echo "Not all Boost libraries built properly."

mkdir -p %{buildroot}%{_docdir}

pushd %{buildroot}%{_libdir}
blibs=$(find . -name \*.so.%{version})
echo $blibs | xargs chrpath -d 

for lib in ${blibs}; do
  BASE=$(basename ${lib} .so.%{version})
  SONAME_MT="$BASE-mt.so"
  ln -sf ${lib} $SONAME_MT
done
popd

#install the man pages
rm -rf doc/man/man3/boost::units::operator

for sec in 3 7 9; do
    install -d %buildroot/%{_mandir}/man${sec}
done

#install doc files
dos2unix libs/ptr_container/doc/tutorial_example.html \
	libs/parameter/doc/html/reference.html \
	libs/parameter/doc/html/index.html \
	libs/iostreams/doc/tree/tree.js \
	libs/graph/doc/lengauer_tarjan_dominator.htm \
	libs/test/test/test_files/errors_handling_test.pattern \
	libs/test/test/test_files/result_report_test.pattern
find . -name \*.htm\* -o -name \*.gif -o -name \*.css -o -name \*.jpg -o -name \*.png -o -name \*.ico | \
	tar --files-from=%{S:4} -cf - --files-from=- | tar -C %{buildroot}%{_docdir} -xf -
rm -rf %{buildroot}%{_docdir}/boost
ln -s /usr/include/boost %{buildroot}%{_docdir}
ln -s ../LICENSE_1_0.txt %{buildroot}%{_docdir}/libs
#Copy the news file.
#cp %%{S:5} %%{buildroot}%%{_docdir}
#only for documentation, doesn't need to be executable
find %{buildroot}%{_docdir} -name \*.py -exec chmod -x {} +
rm -f %{buildroot}%{_libdir}/*.a
#symlink dupes
%fdupes %buildroot

%remove_docs


%post -n libboost_date_time -p /sbin/ldconfig
%post -n libboost_filesystem -p /sbin/ldconfig
%post -n libboost_iostreams -p /sbin/ldconfig
%post -n libboost_test -p /sbin/ldconfig
%post -n libboost_program_options -p /sbin/ldconfig
%post -n libboost_python -p /sbin/ldconfig
%post -n libboost_regex -p /sbin/ldconfig
%post -n libboost_serialization -p /sbin/ldconfig
%post -n libboost_signals -p /sbin/ldconfig
%post -n libboost_thread -p /sbin/ldconfig
%post -n libboost_math -p /sbin/ldconfig 

%if %build_mpi
%post -n libboost_mpi -p /sbin/ldconfig       
%endif

%post -n libboost_graph -p /sbin/ldconfig
%post -n libboost_system -p /sbin/ldconfig
%post -n libboost_wave -p /sbin/ldconfig
%post -n libboost_random -p /sbin/ldconfig
%post -n libboost_chrono -p /sbin/ldconfig
%post -n libboost_locale -p /sbin/ldconfig
%post -n libboost_timer -p /sbin/ldconfig

%postun -n libboost_date_time -p /sbin/ldconfig
%postun -n libboost_filesystem -p /sbin/ldconfig
%postun -n libboost_iostreams -p /sbin/ldconfig
%postun -n libboost_test -p /sbin/ldconfig
%postun -n libboost_program_options -p /sbin/ldconfig
%postun -n libboost_python -p /sbin/ldconfig
%postun -n libboost_regex -p /sbin/ldconfig
%postun -n libboost_serialization -p /sbin/ldconfig
%postun -n libboost_signals -p /sbin/ldconfig
%postun -n libboost_thread -p /sbin/ldconfig
%postun -n libboost_math -p /sbin/ldconfig

%if %build_mpi
%postun -n libboost_mpi -p /sbin/ldconfig
%endif

%postun -n libboost_graph -p /sbin/ldconfig
%postun -n libboost_system -p /sbin/ldconfig
%postun -n libboost_wave -p /sbin/ldconfig
%postun -n libboost_random -p /sbin/ldconfig
%postun -n libboost_chrono -p /sbin/ldconfig
%postun -n libboost_locale -p /sbin/ldconfig
%postun -n libboost_timer -p /sbin/ldconfig

%files -n boost-license
%defattr(-, root, root, -)
##%doc %{_docdir}/LICENSE_1_0.txt

%files -n libboost_date_time
%defattr(-, root, root, -)
%{_libdir}/libboost_date_time*.so.*

%files -n libboost_filesystem
%defattr(-, root, root, -)
%{_libdir}/libboost_filesystem*.so.*

%files -n libboost_graph
%defattr(-, root, root, -)
%{_libdir}/libboost_graph*.so.*

%files -n libboost_iostreams
%defattr(-, root, root, -)
%{_libdir}/libboost_iostreams*.so.*

%files -n libboost_math
%defattr(-, root, root, -)
%{_libdir}/libboost_math_*.so.*

%if %build_mpi

%files -n libboost_mpi
%defattr(-, root, root, -)
%{_libdir}/libboost_mpi*.so.*
%{_libdir}/mpi.so
%endif

%files -n libboost_test
%defattr(-, root, root, -)
%{_libdir}/libboost_prg_exec_monitor*.so.*
%{_libdir}/libboost_unit_test_framework*.so.*

%files -n libboost_program_options
%defattr(-, root, root, -)
%{_libdir}/libboost_program_options*.so.*

%files -n libboost_python
%defattr(-, root, root, -)
%{_libdir}/libboost_python*.so.*

%files -n libboost_serialization
%defattr(-, root, root, -)
%{_libdir}/libboost_*serialization*.so.*

%files -n libboost_signals
%defattr(-, root, root, -)
%{_libdir}/libboost_signals*.so.*

%files -n libboost_system
%defattr(-, root, root, -)
%{_libdir}/libboost_system*.so.*

%files -n libboost_thread
%defattr(-, root, root, -)
%{_libdir}/libboost_thread*.so.*

%files -n libboost_wave
%defattr(-, root, root, -)
%{_libdir}/libboost_wave*.so.*

%files -n libboost_regex
%defattr(-, root, root, -)
%{_libdir}/libboost_regex*.so.*

%files -n libboost_random
%defattr(-, root, root, -)
%{_libdir}/libboost_random*.so.*

%files -n libboost_chrono
%defattr(-, root, root, -)
%{_libdir}/libboost_chrono*.so.*

%files -n libboost_locale
%defattr(-, root, root, -)
%{_libdir}/libboost_locale*.so.*

%files -n libboost_timer
%defattr(-, root, root, -)
%{_libdir}/libboost_timer*.so.*

%files devel
%defattr(-, root, root, -)
%{_includedir}/boost
%{_libdir}/*.so
%if %build_mpi
%exclude %{_libdir}/mpi.so
%endif
#%%{_datadir}/aclocal/*.m4


%changelog
