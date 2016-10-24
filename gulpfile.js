var gulp = require('gulp');

gulp.task('default', function() {
  // place code for your default task here
  console.log('gulping');

  gulp.src([
    'node_modules/vue/dist/vue.js',
    'node_modules/vue/dist/vue.min.js'
  ]).pipe(gulp.dest('./mainsite/static/mainsite/vendor/vue/'));

  gulp.src([
    'node_modules/fullcalendar/dist/fullcalendar.js',
    'node_modules/fullcalendar/dist/fullcalendar.min.js',
    'node_modules/fullcalendar/dist/fullcalendar.css',
    'node_modules/fullcalendar/dist/fullcalendar.min.css'
  ]).pipe(gulp.dest('./mainsite/static/mainsite/vendor/fullcalendar/'));

  gulp.src([
    'node_modules/bootstrap/dist/css/*',
  ]).pipe(gulp.dest('./mainsite/static/mainsite/vendor/bootstrap/css'));

  gulp.src([
    'node_modules/bootstrap/dist/fonts/*',
  ]).pipe(gulp.dest('./mainsite/static/mainsite/vendor/bootstrap/fonts'));

  gulp.src([
    'node_modules/bootstrap/dist/js/*',
  ]).pipe(gulp.dest('./mainsite/static/mainsite/vendor/bootstrap/js'));

  gulp.src([
    'node_modules/jquery/dist/*'
  ]).pipe(gulp.dest('./mainsite/static/mainsite/vendor/jquery/'));

  console.log('gulped');
});
