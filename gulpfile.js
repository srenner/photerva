var gulp = require('gulp');

gulp.task('default', function() {
  // place code for your default task here
  console.log('gulping');

  gulp.src([
    'node_modules/vue/dist/vue.js',
    'node_modules/vue/dist/vue.min.js',
    'node_modules/fullcalendar/dist/fullcalendar.js',
    'node_modules/fullcalendar/dist/fullcalendar.min.js'
  ]).pipe(gulp.dest('./mainsite/static/mainsite/js/vendor/'));

  gulp.src([
    'node_modules/fullcalendar/dist/fullcalendar.css',
    'node_modules/fullcalendar/dist/fullcalendar.min.css'
  ]).pipe(gulp.dest('./mainsite/static/mainsite/css/vendor/'));

  console.log('gulped');
});
